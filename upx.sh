set -e

mkdir -p ~/.ssh
echo "$SSH_KEY" > ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa
chmod 700 ~/.ssh

rsync -e "ssh -o StrictHostKeyChecking=no" -az jeremyphoward@ps625762.dreamhostps.com:files.fast.ai/hugo-full/$DEST_OS/hugo ./ 
upx hugo

rsync -e "ssh -o StrictHostKeyChecking=no" -az hugo jeremyphoward@ps625762.dreamhostps.com:files.fast.ai/hugo-full/$DEST_OS/
