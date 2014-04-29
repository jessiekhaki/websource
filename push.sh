#!/bin/sh
echo "StrictHostKeyChecking no" >> ~/.ssh/config
cd ..

git config --global user.email "barry@rowlingson.com"
git config --global user.name "Barry Rowlingson"

git clone https://$GITKEY:x-oauth-basic@github.com/chicas-lancaster/chicas-lancaster.github.io.git >/dev/null 2>&1
cd websource
hyde gen -r
hyde publish
