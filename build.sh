git clone https://github.com/gohugoio/hugo.git
cd hugo
latesttag=$(git describe --tags)
git checkout ${latesttag}
patch -p1 < ../hugo.patch
go build --tags extended
[[ "$OSTYPE" == "darwin"* ]] && brew install upx
upx hugo
pwd
