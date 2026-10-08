"""Integrity checks for an externally stored recovered-content package."""
import argparse,base64,hashlib,json,pathlib,struct,zlib
ap=argparse.ArgumentParser();ap.add_argument('content',type=pathlib.Path);ap.add_argument('--indexes',type=pathlib.Path,required=True);a=ap.parse_args();root=a.content
sha=lambda b:hashlib.sha256(b).hexdigest();count=mc=fr=blocks=resources=0;allids=set()
for p in root.glob('*-en.json'):
 d=json.loads(p.read_text())
 if 'source' not in d:continue
 cid=d['id'];b=(root/'originals'/cid/pathlib.Path(d['source']['path']).name).read_bytes();assert sha(b)==d['source']['sha256'];idx=json.loads((a.indexes/(cid+'.json')).read_text());assert {i['id'] for i in idx['items']}=={i['id'] for i in d['items']}
 for i in d['items']:
  assert not i['verified_for_use'];assert i['question_block_indices'];assert i['answer_block_indices'] or i['other_answer_block_indices'];assert i['id'] not in allids;allids.add(i['id']);count+=1
  for v in i['blocks']:
   raw=base64.b64decode(v['raw_base64'],validate=True);assert raw==b[v['source_offset']:v['source_offset']+v['length']] and sha(raw)==v['sha256'];blocks+=1
 for r in d['bank_resources']:
  raw=base64.b64decode(r['raw_base64'],validate=True);off=r['source_offset'];assert raw==b[off+4:off+4+r['length']] and sha(raw)==r['sha256'];resources+=1
for cid in ['course-1-en','intermediate-4-en']:
 d=json.loads((root/(cid+'.json')).read_text());idx=json.loads((a.indexes/(cid+'.json')).read_text());assert {i['id'] for i in idx['items']}=={i['id'] for i in d['items']};banks={}
 for s in d['sources']:
  raw=(root/'originals'/cid/pathlib.Path(s['path']).name).read_bytes();assert sha(raw)==s['sha256'];b=zlib.decompress(raw[16:]);assert sha(b)==s['decompressed_sha256'];banks[s['bank_id']]=b
 lessons={l['id'] for l in idx['lessons']}|{l['id'] for l in d['new_lessons']}
 for i in d['items']:
  assert i['id'] not in allids;allids.add(i['id']);count+=1;assert i['lesson_id'] in lessons;assert not i['verified_for_use'] and not i['rendering_complete'];b=banks[i['source_bank_id']];off=i['question_rich_data_offset'];n=i['question_rich_data_length'];assert sha(b[off:off+n])==i['question_rich_data_sha256'];answer=i['answer']
  if answer['kind']=='choice':
   mc+=1;labels={c['label'] for c in i['choices_in_source_layout_order']};assert answer['label'] in labels;assert chr(97+struct.unpack_from('<I',b,answer['source_index_offset'])[0])==answer['label']
  else:
   fr+=1;t=answer['text_with_controls'];off=answer['source_text_offset'];assert b[off:off+len(t.encode('utf-16le'))].decode('utf-16le')==t
assert (count,mc,fr)==(5425,1250,1491)
# Independently solved fixed examples, not general correctness certification.
d=json.loads((root/'course-1-en.json').read_text());answers={i['source_id']:i['answer']['text_with_controls'] for i in d['items']}
expected={'C1_S01_00085':str(320//4),'C1_S01_00086':'miles','C1_S01_00088':'2 m','C1_S01_00090':str(64//4)+' cm','C1_S01_00091':str(8*8),'C1_S01_00092':'4321','C1_S01_00093':str(3675+285+1308),'C1_S01_00094':'$'+format((500-285)/100,'.2f'),'C1_S01_00095':str(3*12-1)}
for k,v in expected.items():assert answers[k]==v,(k,answers[k],v)
print(json.dumps({'result':'passed','records':count,'multiple_choice_keys':mc,'free_response_blocks':fr,'legacy_blocks_compared_to_source':blocks,'bank_resources_compared_to_source':resources,'independently_checked_fixed_examples':len(expected)}))
