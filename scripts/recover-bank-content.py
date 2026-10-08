"""Bounded binary recovery. Does not execute scripts or certify rendered questions."""
import argparse,base64,collections,hashlib,json,pathlib,re,shutil,struct,zlib
U=lambda b,p:struct.unpack_from('>I',b,p)[0]
L=lambda b,p:struct.unpack_from('<I',b,p)[0]
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')
def lp(b,p):
 n=U(b,p);assert p+4+n<=len(b);return b[p+4:p+4+n]
def text(b):return b.decode('cp1252',errors='replace').replace('\r\n','\n').replace('\r','\n')
def rich_runs(b):
 runs=[]
 for m in re.finditer(rb'\x030002([0-9A-F]{8})00000000\x00([0-9A-F]+),',b):
  n=int(m.group(2),16);assert m.end()+n<=len(b);runs.append({'offset_in_payload':m.end(),'text':text(b[m.end():m.end()+n])})
 return runs

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=pathlib.Path,required=True);ap.add_argument('--indexes',type=pathlib.Path,required=True);ap.add_argument('--output',type=pathlib.Path,required=True);ap.add_argument('--metadata-output',type=pathlib.Path,required=True);a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True);a.metadata_output.mkdir(parents=True,exist_ok=True)
 summary={'version':'0.2.0','scope':'binary/text recovery; no rendering or mathematical certification','courses':[],'ready_for_generation':0};overlays=[]
 for cid,src in [('course-87-en','recovery-v0.2/bank-87/SB87/SB87._bk'),('algebra-1-en','work/algebra1/SMA1/Sma1._bk'),('algebra-2-en','work/algebra2/SMA2/Sma2._bk'),('algebra-half-en','work/algebra_half/SMAH/Smah._bk')]:
  path=a.source_root/src;b=path.read_bytes();source={'path':src,'sha256':sha(b)};dest=a.output/'originals'/cid/path.name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
  idx=json.loads((a.indexes/(cid+'.json')).read_text());bycode={i['source_id']:i for i in idx['items']};bynode={i.get('source_node_id'):i for i in idx['items']};items=[];assets=[];start=52+U(b,48);end=U(b,52);assert (end-start)%46==0
  for at in range(start,end,46):
   r=b[at:at+46]
   if r[0]!=4:continue
   nid=U(r,6);code=text(r[32:44]).strip();identity=bycode[code] if cid=='course-87-en' else bynode[nid];assert code==identity['source_id'];off=U(r,24);body=lp(b,off);pos=0;blocks=[]
   while pos<len(body):
    raw=lp(body,pos);assert len(raw)>=2;typ,fmt=raw[:2];payload=raw[2:];runs=rich_runs(payload) if fmt==1 else [];tx=text(payload) if fmt==0 else '\n'.join(x['text'] for x in runs)
    blocks.append({'type':typ,'format':fmt,'source_offset':off+4+pos+4,'length':len(raw),'sha256':sha(raw),'text':tx,'rich_text_runs':runs,'raw_base64':base64.b64encode(raw).decode()});pos+=4+len(raw)
   assert pos==len(body)
   items.append({'id':identity['id'],'source_id':code,'source_node_id':nid,'lesson_id':identity['lesson_id'],'title':text(lp(b,U(r,16))[10:]),'source_body_offset':off,'blocks':blocks,'question_block_indices':[j for j,v in enumerate(blocks) if v['type'] in (1,4)],'answer_block_indices':[j for j,v in enumerate(blocks) if v['type']==6],'other_answer_block_indices':[j for j,v in enumerate(blocks) if v['type'] in (5,8)],'script_block_indices':[j for j,v in enumerate(blocks) if v['type']==3],'verified_for_use':False})
  for at in range(52,start-4,40):
   off=U(b,at);kind=int.from_bytes(b[at+4:at+6],'big');name=text(b[at+8:at+40]).rstrip('\0');v=lp(b,off);assets.append({'name':name,'kind':kind,'source_offset':off,'length':len(v),'sha256':sha(v),'text':text(v) if kind==1 else None,'raw_base64':base64.b64encode(v).decode()})
  assert len(items)==len(idx['items']);save(a.output/(cid+'.json'),{'id':cid,'source':source,'items':items,'bank_resources':assets})
  summary['courses'].append({'id':cid,'items':len(items),'question_block_records':sum(bool(i['question_block_indices']) for i in items),'answer_block_records':sum(bool(i['answer_block_indices']) for i in items),'answer_or_choice_records':sum(bool(i['answer_block_indices'] or i['other_answer_block_indices']) for i in items),'choice_only_key_unverified':sum(not i['answer_block_indices'] for i in items),'script_records':sum(any(i['blocks'][j]['text'] for j in i['script_block_indices']) for i in items),'rich_object_records':sum(any(v['format']==1 for v in i['blocks']) for i in items),'binary_bank_resources':sum(x['kind']!=1 for x in assets),'source_sha256':source['sha256']})
 inv=json.loads((a.source_root/'ExamView-Extraction/bank-inventory.json').read_text())
 for cid in ['course-1-en','course-1-es','intermediate-4-en','intermediate-4-es']:
  idx=json.loads((a.indexes/(cid+'.json')).read_text());outitems=[];newlessons={};updates=[];stats=collections.Counter();sources=[]
  for bank in idx['source_banks']:
   path=a.source_root/'ExamView-Extraction/original-banks'/bank['source_path'];raw=path.read_bytes();assert sha(raw)==bank['sha256'];b=zlib.decompress(raw[16:]);source={'bank_id':bank['id'],'path':bank['source_path'],'sha256':sha(raw),'decompressed_sha256':sha(b)};sources.append(source);dest=a.output/'originals'/cid/path.name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
   byend={}
   for m in re.finditer(re.escape(b[:4]),b):
    at=m.start()
    if at+520>len(b):continue
    n=L(b,at+516)
    if 4<=n<5000 and at+516+n<len(b):byend[at+516+n]=at
   selected=[i for i in idx['items'] if i['source_bank_id']==bank['id']]
   for identity in selected:
    ip=identity['recovered_text_offset'];iend=ip+len(identity['source_id'])*2+2;assert b[ip:iend-2].decode('utf-16le')==identity['source_id'];start=byend[iend];assert L(b,start+4)==1;metadata=b[start+520:iend].decode('utf-16le').split('\0');assert metadata[-2]==identity['source_id'];label=metadata[0]
    lessonid=bank['id']+':scope:'+sha(label.encode())[:16];old=[l for l in idx['lessons'] if l['id']==lessonid]
    if not old:newlessons[lessonid]={'id':lessonid,'source_bank_id':bank['id'],'label':label,'association':'item_record_metadata'}
    dynlen=L(b,iend);q=iend+dynlen;size,version,n=struct.unpack_from('<3I',b,q);assert version==1 and n*2+56<=size and q+4+size<=len(b);qend=q+4+size;qt=b[q+60:q+60+n*2].decode('utf-16le');typ=L(b,start+8);assert typ in (0,1)
    answer=None;choices=[];stem=qt
    if typ==0:
     count=L(b,start+20);key=L(b,start+12);assert 2<=count<=26 and key<count
     matches=[m for m in re.finditer(r'(?:\x10|\x11)([A-Za-z])\.?\x11',qt) if 0<=ord(m.group(1).lower())-97<count]
     assert len(matches)==count and {m.group(1).lower() for m in matches}==set(chr(97+x) for x in range(count))
     stem=qt[:matches[0].start()]
     for j,m in enumerate(matches):choices.append({'label':m.group(1).lower(),'text_with_controls':qt[m.end():matches[j+1].start() if j+1<len(matches) else len(qt)].rstrip('\x11')})
     correct=chr(97+key);answer={'kind':'choice','label':correct,'text_with_controls':next(c['text_with_controls'] for c in choices if c['label']==correct),'source_index_offset':start+12,'status':'source_key_linked; mathematical correctness not globally verified'};stats['multiple_choice']+=1
    else:
     av,an=struct.unpack_from('<2I',b,qend);assert av==1 and an<100000 and qend+56+an*2<=len(b);answer={'kind':'free_response','text_with_controls':b[qend+56:qend+56+an*2].decode('utf-16le'),'source_text_offset':qend+56,'status':'source_answer_block_linked; mathematical correctness not globally verified'};stats['free_response']+=1
    stats['dynamic_records']+=dynlen>4;stats['question_object_markers']+='\x0f' in qt;stats['new_lesson_link_records']+=not bool(old)
    outitems.append({'id':identity['id'],'source_id':identity['source_id'],'source_bank_id':bank['id'],'source_record_offset':start,'lesson_id':lessonid,'source_metadata_fields':metadata[:-1],'question_text_with_controls':qt,'stem_text_with_controls':stem,'choices_in_source_layout_order':choices,'answer':answer,'dynamic_data_offset':iend,'dynamic_data_length':dynlen,'dynamic_data_sha256':sha(b[iend:iend+dynlen]),'question_rich_data_offset':q+4,'question_rich_data_length':size,'question_rich_data_sha256':sha(b[q+4:qend]),'object_placeholder_count':qt.count('\x0f'),'rendering_complete':False,'verified_for_use':False})
    updates.append({'id':identity['id'],'lesson_id':lessonid,'source_record_offset':start,'metadata_offset':start+520,'question_text_offset':q+60,'answer_link_status':'source_key_or_answer_block_linked','rendering_complete':False,'verified_for_use':False})
  save(a.output/(cid+'.json'),{'id':cid,'sources':sources,'items':outitems,'new_lessons':list(newlessons.values()),'limitations':'Controls and rich rendering data remain authoritative. Plain text alone can omit positioned graphics and math styling. No legacy script execution.'})
  save(a.metadata_output/(cid+'-links.json'),{'id':cid,'base_index_version':'0.1.0','new_lessons':list(newlessons.values()),'sources':sources,'items':updates});summary['courses'].append({'id':cid,'items':len(outitems),'linked_answers':len(outitems),'new_lesson_labels':len(newlessons),**stats})
 save(a.output/'summary.json',summary);save(a.metadata_output/'summary.json',summary);print(json.dumps(summary))
if __name__=='__main__':main()
