from fastcore.utils import *

repo = 'hugo'
rels = urljson(f'https://api.github.com/repos/gohugoio/{repo}/releases/latest')
with urlopen(rels['tarball_url']) as f: untar_dir(f, repo)
run(f'patch -l -p1 -d {repo} -i ../hugo.patch')
run('go build --tags extended')
