#!/usr/bin/env python

from fastcore.utils import *
from ghapi import *
import tarfile

"""
# For testing
context_needs = {'prebuild': {'outputs': {'out': '{\n'
                                 '  "step1": {\n'
                                 '    "outputs": {\n'
                                 '      "tag": "v0.79.0"\n'
                                 '    },\n'
                                 '    "outcome": "success",\n'
                                 '    "conclusion": "success"\n'
                                 '  }\n'
                                 '}'},
              'result': 'success'}}
"""

platform = dict(linux='linux', linux2='linux', win32='win', darwin='mac')[sys.platform]
out = loads(nested_idx(context_needs, 'prebuild', 'outputs', 'out'))
tag = nested_idx(out, 'step1', 'outputs', 'tag')
if not tag: sys.exit()

rel = GhApi().repos.get_release_by_tag(owner='gohugoio', repo='hugo', tag=tag)
with urlopen(rel.tarball_url) as f: untar_dir(f, 'hugo')
os.chdir('hugo')
run(f'patch -l -p1 -i ../hugo.patch')
run('go build --tags extended')
ext_nm = 'hugo.exe' if platform=='win' else 'hugo'
fn = f'hugo-{platform}.tgz'
with tarfile.open(fn, "w:gz") as tar: tar.add(ext_nm)

api = GhApi(owner='fastai', repo='hugo-mathjax', token=github_token())
rel = api.repos.get_release_by_tag(tag)
api.upload_file(rel, fn)
