"""Validate shipped metadata, links, provenance and conservative readiness."""
import hashlib,json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]/'data/course-banks/v0.1'
c=json.loads((root/'catalog.json').read_text());expected={'course-87-en':789,'algebra-1-en':679,'algebra-2-en':592,'algebra-half-en':624,'course-1-en':1353,'course-1-es':1353,'intermediate-4-en':1388,'intermediate-4-es':1388}
assert len(c['courses'])==6 and len(c['banks'])==8
ids=set();unresolved=0;empty=[]
for b in c['banks']:
 p=root/b['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==b['sha256'];d=json.loads(p.read_text());assert len(d['items'])==expected[b['id']]
 assert d['readiness']['metadata_indexed'] and not d['readiness']['verified_for_use'] and not d['readiness']['generator_implemented']
 assert d['standards']==[]
 lessons={x['id'] for x in d['lessons']};assert len(lessons)==len(d['lessons']);banks={x['id'] for x in d['source_banks']};used=set()
 for i in d['items']:
  assert i['id'] not in ids;ids.add(i['id']);assert i['source_id']
  assert not any(k in i for k in ['prompt','answer','script','student','student_name'])
  if i['lesson_id'] is None:
   unresolved+=1;assert i['lesson_link_status']=='unresolved' and i['source_bank_id'] in banks
  else:assert i['lesson_id'] in lessons;used.add(i['lesson_id'])
 if d['id'].startswith('algebra'):
  for l in d['lessons']:
   actual=sum(i['lesson_id']==l['id'] for i in d['items']);assert actual==l['source_item_count']
   if not actual:empty.append(l['id'])
assert len(ids)==8166 and unresolved==5482
assert 'algebra-2-en:scope:128' in empty
assert c['totals']['lesson_records']==1044
print(json.dumps({'result':'passed','unique_item_records':len(ids),'unresolved_examview_lesson_links':unresolved,'empty_algebra_scopes':empty,'catalog_hashes':'passed'}))
