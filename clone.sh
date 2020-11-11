git clone https://github.com/gohugoio/hugo.git
cd hugo
latesttag=$(git describe --tags)
git checkout ${latesttag}
patch -p1 < ../hugo.patch
