from fastcore.utils import *
import os

repo = 'hugo'
rels = urljson(f'https://api.github.com/repos/gohugoio/{repo}/releases/latest')
with urlopen(rels['tarball_url']) as f: untar_dir(f, repo)
os.chdir(repo)
run(f'patch -l -p1 -i ../hugo.patch')
run('go build --tags extended')
