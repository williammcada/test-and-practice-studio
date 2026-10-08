"""Check actual browser-produced synthetic exports; run after phase3-exports.cjs."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import json
root=Path(__file__).resolve().parents[1]
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
results=[]
for name in ['A4-1-student','A4-1-key','Letter-2-student','Letter-2-key']:
 with ZipFile(root/'artifacts/phase3'/f'{name}.docx') as z:
  doc=ET.fromstring(z.read('word/document.xml'))
  body=doc.find('w:body',ns)
  blocks=body.findall('w:tbl',ns)
  assert len(blocks)==11,(name,'question blocks')
  assert all(b.find('w:tr/w:trPr/w:cantSplit',ns) is not None for b in blocks)
  assert len(doc.findall('.//m:oMath',ns))==3
  assert len(doc.findall('.//w:tbl',ns))==12 # 11 questions plus one function table
  assert not doc.findall('.//w:p/w:p',ns)
  text=''.join(doc.itertext())
  assert ('Answer:' in text)==name.endswith('key')
  for n,learner in [(1,'Synthetic Learner A'),(2,'Synthetic Learner B')]:
   footer=ET.fromstring(z.read(f'word/footer{n}.xml'))
   assert learner in ''.join(footer.itertext())
  for f in z.namelist():
   if f.endswith('.xml') or f.endswith('.rels'):ET.fromstring(z.read(f))
  results.append({'file':name+'.docx','questions':len(blocks),'nativeEquations':3,'dataTables':1,'studentKeyIsolation':'passed','learnerFooters':'passed'})
print(json.dumps({'result':'passed','exports':results}))
