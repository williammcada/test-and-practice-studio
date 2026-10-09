"""Deterministically bundle the metadata review UI; no publisher question bodies."""
import pathlib,json,hashlib,gzip,base64,subprocess
root=pathlib.Path(__file__).resolve().parents[1];pin=json.loads((root/'vendor/math-engine-provenance.json').read_text());assert hashlib.sha256((root/'vendor/course-banks.js').read_bytes()).hexdigest()==pin['sha256'];base=root/'data/course-banks/v0.1';catalog=json.loads((base/'catalog.json').read_text());version=json.loads((root/'package.json').read_text())['version'];assert ("VERSION='"+version+"'") in (root/'src/core.js').read_text();result={'version':version,'catalog':'course-index-0.1+recovery-0.2','banks':[],'contentHashes':json.loads((root/'data/recovery/v0.2/content-hashes.json').read_text())}
placements=json.loads(subprocess.check_output(['node','-e',"console.log(JSON.stringify(require('./vendor/cross-course').coursePlacement))"],cwd=root))
placements={p['bankId']:p for p in placements}
for entry in catalog['banks']:
 assert entry['language']=='en'
 p=base/entry['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'];d=json.loads(p.read_text());lessons={l['id']:dict(l) for l in d['lessons']};items={i['id']:dict(i) for i in d['items']};overlay=root/'data/recovery/v0.2'/(d['id']+'-links.json')
 if overlay.exists():
  o=json.loads(overlay.read_text());assert o['id']==d['id'] and len(o['items'])==len(items)
  for s in o['sources']:assert next(b for b in d['source_banks'] if b['id']==s['bank_id'])['sha256']==s['sha256']
  for l in o['new_lessons']:lessons[l['id']]=l
  for i in o['items']:assert i['id'] in items;items[i['id']].update(i)
 names={c['id']:c['name'] for c in catalog['courses']};newitems=[]
 for i in items.values():
  assert i['lesson_id'] in lessons
  newitems.append({'id':i['id'],'sourceId':i['source_id'],'bankId':d['id'],'lessonId':i['lesson_id'],'title':i.get('title','')})
 newlessons=[]
 for l in lessons.values():
  label=l.get('label') or ('Lesson / topic '+str(l.get('source_number','')))
  title=l.get('title')
  display=label+(': '+title if title and title!=label else '')
  newlessons.append({'id':l['id'],'display':display,'count':sum(i['lessonId']==l['id'] for i in newitems)})
 # Natural label order, retaining bank-scoped duplicate lesson labels.
 import re
 newlessons.sort(key=lambda l:[int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)',l['display'])])
 placement=placements[d['id']];label='Grade '+str(placement['localGrade']) if placement['placement']=='grade-assigned' else 'Tracked · not grade-locked'
 result['banks'].append({'id':d['id'],'display':names[d['course_id']]+' · '+label+' · English','localGrade':placement['localGrade'],'placement':placement['placement'],'lessons':newlessons,'items':newitems})
assert sum(len(b['items']) for b in result['banks'])==5425
result['legacyRecordCount']=5425
authored=json.loads(subprocess.check_output(['node','-e',"const E=require('./vendor/course-banks');console.log(JSON.stringify(E.catalog.filter(c=>c.origin==='original-curriculum-task')))"],cwd=root))
for c in authored:
 b=next(b for b in result['banks'] if b['id']==c['sourceId'].split(':authored:')[0])
 assert ':authored:' in c['sourceId'] and all(i['id']!=c['sourceId'] for i in b['items'])
 lesson=next(l for l in b['lessons'] if l['id']==c['lessonId'])
 b['items'].append({'id':c['sourceId'],'sourceId':c['sourceLabel'],'bankId':b['id'],'lessonId':c['lessonId'],'title':c['title'],'origin':c['origin'],'standard':c['standard'],'alias':c['alias']})
 lesson['count']+=1
result['authoredRecordCount']=len(authored)
assert sum(len(b['items']) for b in result['banks'])==5425+len(authored)
packed=base64.b64encode(gzip.compress(json.dumps(result,ensure_ascii=False,separators=(',',':')).encode(),mtime=0)).decode();html=(root/'src/index.template.html').read_text()
for f,h in pin['files'].items():assert hashlib.sha256((root/'vendor'/f).read_bytes()).hexdigest()==h
html=html.replace('/*ENGINE*/','\n'.join((root/'vendor'/f).read_text() for f in pin['files']))
for token,path in [('/*CONNECTIONS*/','connections-ui.js'),('/*STYLES*/','studio.css'),('/*CORE*/','core.js'),('/*APP*/','app.js'),('/*ZIP*/','../vendor/third-party/jszip-3.10.1.min.js'),('/*PACKETCORE*/','packet-core.js'),('/*PACKETIO*/','packet-io.js'),('/*PACKETUI*/','packet-ui.js'),('/*ENGINE*/','../vendor/course-banks.js')]:html=html.replace(token,(root/'src'/path).read_text())
html=html.replace('/*CATALOG*/',packed).replace('/*VERSION*/',version);assert ('<title>Test and Practice Studio v'+version) in html;assert ('class="version">v'+version) in html;(root/'index.html').write_text(html);delivery=root/'downloads'/('Test-and-Practice-Studio-v'+version+'.html');delivery.parent.mkdir(exist_ok=True);assert not delivery.exists() or delivery.read_bytes()==html.encode(), 'Changed HTML must use a new version';delivery.write_text(html);print('Built index.html:',len(html.encode()),'bytes;',5425,'legacy items +',len(authored),'authored tasks')
