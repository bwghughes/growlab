#!/bin/bash
python3 app.py

export GIT_SSH_COMMAND="ssh -i `pwd`/.ssh/id_rsa"

cp html/* ./docs/
cd docs

git add .

git commit -s -m "Update images at `date`"
git pull origin master --rebase
git push origin master

s3cmd put $(pwd)/preview.jpg s3://growlab-archive/image-$(date -d "today" +"%Y%m%d%H%M").jpg

