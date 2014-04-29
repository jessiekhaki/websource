#!/bin/sh
echo "StrictHostKeyChecking no" >> ~/.ssh/config
cd ..
git clone https://$GITKEY:x-oauth-basic@github.com/chicas-lancaster/chicas-lancaster.github.io.git
cd websource
hyde gen -r
hyde publish
