all:
	rm -f */*/*~
	hyde gen

force:
	rm -f */*/*~
	hyde gen -r

serve:
	(cd deploy ; python -m SimpleHTTPServer & )


publish:
	rm -f */*/*~
	hyde gen -r
	hyde publish

travis:
	sudo apt-get install python-dev libffi-dev libssl-dev
	pip install pyopenssl ndg-httpsclient pyasn1
	pip install -r requirements.txt
	./push.sh

stagecopy:
	cp -r deploy/* ../chicas.gitlab.io/
	./tools/stagify.sh ../chicas.gitlab.io/
stagepush:
	cd ../chicas.gitlab.io/ && \
	git add . && \
	git commit -a -m 'staging push' && \
	git push

# Convert poster PDFs to thumbnails with:
# convert  -geometry 190x -background white -alpha remove -crop 190x100+0+0 foo.pdf foo.png

