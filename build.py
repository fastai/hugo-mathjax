from fastcore.utils import *
from urllib.request import urlopen
import tarfile

user,repo = 'gohugoio','hugo'
rels = urljson(f'https://api.github.com/repos/{user}/{repo}/releases/latest')
dest = Path('hugo-download')
with urlopen(urlwrap(rels['tarball_url'])) as u:
    tarfile.open(mode='r:gz', fileobj=u).extractall(dest)

dest.ls()[0].rename('hugo')
dest.rmdir()
