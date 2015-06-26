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

