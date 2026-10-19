#!/usr/bin/env python3
"""Build self-contained skill references and a deterministic plugin ZIP."""
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('fred', 'characters', 'combat')


def build():
    source = ROOT / 'sources'
    # Only explicit, public source paths enter the distribution.
    for name in SKILLS:
        ref = ROOT / 'skills' / name / 'references'
        ref.mkdir(parents=True, exist_ok=True)
        for folder in ('srd', 'license'):
            dest = ref / folder
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(source / folder, dest)
        for filename in ('index.md', 'entries.md', 'table.md'):
            text = (ROOT / 'docs' / filename).read_text()
            (ref / filename).write_text(text.replace('(../sources/srd/', '(srd/'))
        shutil.copyfile(ROOT / 'THIRD_PARTY_NOTICES.md', ref / 'notices.md')
        procedures = ref / 'procedures'
        procedures.mkdir(exist_ok=True)
        for other in SKILLS:
            text = (ROOT / 'skills' / other / 'SKILL.md').read_text()
            text = text.replace('(references/', '(../')
            (procedures / f'{other}.md').write_text(text)
    version = json.loads((ROOT / 'plugin.json').read_text())['version']
    files = [ROOT / p for p in ('plugin.json', 'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md')]
    files += [p for base in ('assets', 'skills', 'docs', 'sources')
              for p in (ROOT / base).rglob('*') if p.is_file()]
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    artifact = dist / f'fred-{version}.zip'
    with zipfile.ZipFile(artifact, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for path in sorted(files):
            if path.is_symlink():
                raise ValueError(f'Symlink forbidden: {path}')
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            out.writestr(info, path.read_bytes())
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    (dist / f'{artifact.name}.sha256').write_text(f'{digest}  {artifact.name}\n')
    print(f'{artifact.name}: {artifact.stat().st_size} bytes; sha256 {digest}')


if __name__ == '__main__':
    build()
