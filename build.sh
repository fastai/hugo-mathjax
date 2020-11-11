set -e

case "$OSTYPE" in
  darwin*)
    DEST_OS=macos
    ;;
  linux*)
    DEST_OS=linux
    ;;
  *)
    echo "unknown: $OSTYPE"
    ;;
esac

git clone https://github.com/gohugoio/hugo.git
cd hugo
latesttag=$(git describe --tags)
git checkout ${latesttag}
patch -l -p1 < ../hugo.patch
go build --tags extended

mkdir -p ~/.ssh
echo "$SSH_KEY" > ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa
chmod 700 ~/.ssh
rsync -e "ssh -o StrictHostKeyChecking=no" -az hugo jeremyphoward@ps625762.dreamhostps.com:files.fast.ai/hugo-full/$DEST_OS/
