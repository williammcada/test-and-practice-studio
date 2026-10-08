"""Import metadata only. Raw prompts, answers, scripts and student data stay outside git."""
import argparse,collections,csv,hashlib,json,pathlib,re,zipfile
import openpyxl

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def slug(s):return re.sub(r'[^a-z0-9]+','-',str(s).lower()).strip('-')
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=pathlib.Path,required=True);ap.add_argument('--output',type=pathlib.Path,required=True);a=ap.parse_args();root=a.source_root;out=a.output;out.mkdir(parents=True,exist_ok=True)
 readiness={'metadata_indexed':True,'prompt_decoded':'not_imported','math_diagram_rendered':'not_verified','answer_linked':'not_imported','generator_implemented':False,'verified_for_use':False}
 catalog={'schema_version':'0.1.1','scope':'metadata only','courses':[],'banks':[],'readiness_defaults':readiness,'standards_required_for_manual_selection':False,'sources':[]}
 def source(p):
  rec={'path':str(p.relative_to(root)),'sha256':digest(p)};catalog['sources'].append(rec);return rec
 def add(cid,name,language,banks,lessons,items,edition=None,grade=None):
  bid=cid+'-'+language;seen=set()
  for i in items:
   if i['id'] in seen:raise ValueError('Duplicate stable ID '+i['id'])
   seen.add(i['id'])
  d={'schema_version':'0.1.0','id':bid,'course_id':cid,'language':language,'edition':edition,'local_grade':grade,'standards':[],'readiness':readiness,'source_banks':banks,'lessons':lessons,'items':items}
  path=bid+'.json';write(out/path,d)
  catalog['banks'].append({'id':bid,'course_id':cid,'language':language,'path':path,'sha256':digest(out/path),'lesson_count':len(lessons),'item_count':len(items),'source_bank_count':len(banks)})
  if not any(c['id']==cid for c in catalog['courses']):catalog['courses'].append({'id':cid,'name':name,'local_grade':grade})
 p=root/'scope-checkpoint/saxon-87-source-index.json';s=source(p);d=json.loads(p.read_text());wp=root/'source-recovery/Saxon_87_Generator_Scope_Recovery.xlsx';ws=source(wp)
 assert ws['sha256']==d['source_sha256']
 w=openpyxl.load_workbook(wp,read_only=True,data_only=True);lessons=[];lookup={}
 for rownum,r in enumerate(w['Lesson Scope'].values,1):
  if rownum<4 or r[0] is None:continue
  lid='course-87-en:scope:'+str(r[0]);lookup[r[3]]=lid;lessons.append({'id':lid,'source_number':r[2],'kind':r[1],'label':r[3],'title':r[5],'source_row':rownum})
 items=[{'id':'course-87-en:item:'+i['source_id'],'source_id':i['source_id'],'lesson_id':lookup[i['scope_label']],'source_row':i['workbook_row'],'script_present':i['has_script']} for i in d['items']]
 add('course-87','Introduction to PreAlgebra (8/7)','en',[{'id':'course-87-en:source','source':ws,'item_sheet':d['source_sheet'],'lesson_sheet':'Lesson Scope'}],lessons,items,grade=5)
 apath=root/'scope-checkpoint/algebra-source-index.json';source(apath);ai=json.loads(apath.read_text());zp=root/'source-recovery/NEW SAXON TEST & PRACTICE GENERATOR/Saxon_Algebra_Content_Recovery.zip';zs=source(zp);assert zs['sha256']==ai['source_sha256'];z=zipfile.ZipFile(zp)
 for c in ai['courses']:
  key={'Algebra 1':'algebra1','Algebra 2':'algebra2','Algebra 1/2':'algebra_half'}[c['course']];cid={'algebra1':'algebra-1','algebra2':'algebra-2','algebra_half':'algebra-half'}[key];bid=cid+'-en';member='Saxon_Algebra_Content_Recovery/'+key+'/content.json';raw=json.loads(z.read(member));lessons=[{'id':bid+':scope:'+str(l['number']),'source_number':l['number'],'title':l['title'],'source_item_count':l['item_count']} for l in raw['lessons']]
  items=[{'id':bid+':node:'+str(i['source_node_id']),'source_id':i['source_id'],'source_node_id':i['source_node_id'],'lesson_id':bid+':scope:'+str(i['source_lesson']),'body_offset':i['body_offset'],'script_present':i['has_script']} for i in c['items']]
  add(cid,c['course'],'en',[{'id':bid+':source','source':zs,'member':member}],lessons,items,raw['edition'])
 ep=root/'ExamView-Extraction';invp=ep/'bank-inventory.json';source(invp);inventory=json.loads(invp.read_text());ip=ep/'item-id-index.csv';source(ip);rows=list(csv.DictReader(ip.open()));lp=ep/'lesson-index.csv';source(lp);lrows=list(csv.DictReader(lp.open()))
 for cid,name,match in [('course-1','Course 1','Course 1'),('intermediate-4','Intermediate 4','Int4')]:
  for language,folder in [('en','English')]:
   bid=cid+'-'+language;banks=[];lessons=[];items=[]
   for b in inventory:
    path=b['bank']
    if match not in path or '/'+folder+'/' not in path:continue
    bankid=bid+':bank:'+pathlib.PurePosixPath(path).stem;banks.append({'id':bankid,'source_path':path,'sha256':b['sha256'],'title':b['title']})
    for n,l in enumerate(x for x in lrows if x['bank']==path):lessons.append({'id':bankid+':scope:'+hashlib.sha256(l['lesson'].encode()).hexdigest()[:16],'source_bank_id':bankid,'label':l['lesson'],'association':'bank_contains_lesson; individual item links unresolved'})
    for i in (x for x in rows if x['bank']==path):items.append({'id':bankid+':item:'+i['item_id'],'source_id':i['item_id'],'source_bank_id':bankid,'lesson_id':None,'lesson_link_status':'unresolved','recovered_text_offset':int(i['offset']),'script_present':None})
   assert banks,(cid,language)
   add(cid,name,language,banks,lessons,items)
 catalog['totals']={'courses':len(catalog['courses']),'language_banks':len(catalog['banks']),'items':sum(x['item_count'] for x in catalog['banks']),'lesson_records':sum(x['lesson_count'] for x in catalog['banks'])};write(out/'catalog.json',catalog);print(json.dumps(catalog['totals']))
if __name__=='__main__':main()
