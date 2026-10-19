#!/usr/bin/env python3
"""Check release content, source fidelity, local links and isolation boundaries."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('fred', 'characters', 'combat')


def check():
    manifest = json.loads((ROOT / 'sources/manifest.json').read_text())
    expected = manifest['files']
    assert len(expected) == 28
    seen = []
    for item in expected:
        path = ROOT / item['path']
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item['sha256'], path
        # Original page transcriptions have a single trailing newline.
        for part in re.split(r'(?=^# srd-2\.0 — page \d+\n)', raw.decode(), flags=re.M):
            if not part.strip():
                continue
            page = int(re.match(r'# srd-2\.0 — page (\d+)', part)[1])
            data = (part.rstrip() + '\n').encode()
            original = manifest['pages'][page - 1]
            assert original['page'] == page
            assert hashlib.sha256(data).hexdigest() == original['sha256'], f'Page {page}'
            seen.append(page)
    assert seen == list(range(1, 225)), 'Missing, duplicated or reordered source pages'
    for name in SKILLS:
        skill = ROOT / 'skills' / name
        for item in expected:
            assert (skill / 'references/srd' / Path(item['path']).name).read_bytes() == (ROOT / item['path']).read_bytes()
        files = [p for p in skill.rglob('*') if p.is_file()]
        assert len(files) <= 100
        assert sum(p.stat().st_size for p in files) < 5 * 1024 * 1024
        assert all(p.stat().st_size < 1024 * 1024 for p in files)
    for path in ROOT.rglob('*'):
        if any(x in path.parts for x in ('.git', 'dist', '__pycache__', '.local')):
            continue
        assert not path.is_symlink(), path
        if not path.is_file():
            continue
        assert path.suffix not in ('.sqlite', '.db', '.pdf'), path
        if path.suffix in ('.md', '.json', '.yaml'):
            text = path.read_text()
            # Public content must not contain local purchased-source paths.
            assert not re.search(r'/home/|/Users/|Documents/DH|player\.sqlite|master\.sqlite', text), path
        if path.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                target = target.split('#')[0]
                assert (path.parent / target).exists(), f'{path}: broken link {target}'
    package = json.loads((ROOT / 'plugin.json').read_text())
    assert package['name'] == 'fred'
    assert sorted(p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')) == sorted(SKILLS)
    try:
        import jsonschema
    except ImportError:
        print('Optional official-schema check skipped: install jsonschema for development.')
    else:
        jsonschema.validate(package, json.loads((ROOT / 'tests/plugin.schema.json').read_text()))
    artifact = ROOT / 'dist' / f"fred-{package['version']}.zip"
    with zipfile.ZipFile(artifact) as archive:
        assert archive.testzip() is None
        assert 'plugin.json' in archive.namelist()
        assert not any('..' in Path(n).parts for n in archive.namelist())
        for name in SKILLS:
            assert f'skills/{name}/SKILL.md' in archive.namelist()
    print('PASS: 224 source pages in order, 3 complete skill bundles, integrity, links, isolation, manifest and ZIP.')


if __name__ == '__main__':
    check()
