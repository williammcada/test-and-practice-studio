"""Verify complete question/answer structure and diagram media in actual exports."""
from pathlib import Path
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as ET
import json, hashlib, os
from PIL import Image

root = Path(__file__).resolve().parents[1] / 'artifacts/comparison-chunk3'
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
results = []
for name in ['A4-student', 'Letter-key', 'Letter-key-compact']:
    with ZipFile(root / (name + '.docx')) as archive:
        doc = ET.fromstring(archive.read('word/document.xml'))
        text = [t.text or '' for t in doc.findall('.//w:t', ns)]
        numbers = [t for t in text if t in [str(n) + '.' for n in range(1, 13)]]
        assert numbers == [str(n) + '.' for n in range(1, 13)], (name, numbers)
        answers = [t for t in text if t.startswith('Answer:')]
        assert len(answers) == (0 if name == 'A4-student' else 12), (name, answers)
        assert len(doc.findall('.//w:drawing', ns)) == 7
        images = [f for f in archive.namelist() if f.endswith('.png')]
        assert len(images) == 7
        for f in images:
            im = Image.open(BytesIO(archive.read(f)))
            assert min(im.size) >= 400, (f, im.size)
        if name != 'A4-student':
            assert any('SAS; CPCTC' in t for t in text)
            assert any('69; 81; 95' in t for t in text)
        baseline = os.environ.get('COMPARE_BASELINE_EXPORTS')
        unchanged = None
        if baseline:
            with ZipFile(Path(baseline) / (name + '.docx')) as prior:
                for f in archive.namelist():
                    assert archive.read(f) == prior.read(f), (name, f)
                assert sorted(archive.namelist()) == sorted(prior.namelist())
                unchanged = True
        results.append({'file': name + '.docx', 'questions': 12,
                        'answers': len(answers), 'diagrams': len(images),
                        'contentMatchesVisuallyInspectedRc1': unchanged,
                        'sha256': hashlib.sha256((root / (name + '.docx')).read_bytes()).hexdigest(),
                        'result': 'passed'})
(root / 'docx-results.json').write_text(json.dumps(results, indent=2) + '\n')
print(results)
