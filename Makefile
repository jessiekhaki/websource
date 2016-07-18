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
	./push.sh

# Convert poster PDFs to thumbnails with:
# convert  -geometry 190x -background white -alpha remove -crop 190x100+0+0 foo.pdf foo.png

