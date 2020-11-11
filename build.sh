set -e

case "$OSTYPE" in
  darwin*)
    brew install upx rsync
    DEST_OS=macos
    ;;
  linux*)
    sudo apt-get update
    sudo apt-get install -y rsync
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
patch -p1 < ../hugo.patch
go build --tags extended

upx hugo
upx -t hugo

mkdir -p ~/.ssh
echo "$SSH_KEY" > ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa
chmod 700 ~/.ssh
rsync -e "ssh -o StrictHostKeyChecking=no" -az hugo jeremyphoward@ps625762.dreamhostps.com:files.fast.ai/hugo/$DEST_OS/
