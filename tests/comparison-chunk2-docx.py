"""Check that exported graph choices remain labelled, complete, and grouped in Word."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import json
root=Path(__file__).resolve().parents[1]/'artifacts/comparison-chunk2'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
results=[]
for name,expected in [('A4-student',2),('Letter-key',2),('Letter-key-compact',0)]:
 with ZipFile(root/(name+'.docx')) as z:
  doc=ET.fromstring(z.read('word/document.xml'));grids=[]
  for table in doc.findall('.//w:tbl',ns):
   rows=table.findall('w:tr',ns)
   cells=[r.findall('w:tc',ns) for r in rows]
   if len(rows)!=2 or any(len(cs)!=2 for cs in cells):continue
   labels=[]
   for row,cs in zip(rows,cells):
    for cell in cs:
     ts=[t.text or '' for t in cell.findall('.//w:t',ns)]
     labels.extend(t for t in ts if t.startswith('Option '))
   if sorted(labels)!=['Option A','Option B','Option C','Option D']:continue
   for row,cs in zip(rows,cells):
    assert row.find('w:trPr/w:cantSplit',ns) is not None
    for cell in cs:
     assert len(cell.findall('.//w:drawing',ns))==1
     assert len([t for t in cell.findall('.//w:t',ns) if (t.text or '').startswith('Option ')])==1
   grids.append(labels)
  assert len(grids)==expected,(name,len(grids),expected)
  results.append({'file':name+'.docx','completeChoiceGrids':len(grids),'result':'passed'})
(root/'docx-results.json').write_text(json.dumps(results,indent=2)+'\n');print(results)
