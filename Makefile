all:
	rm -f */*/*~
	hyde gen

force:
	rm -f */*/*~
	hyde gen -r

publish:
	rm -f */*/*~
	hyde gen -r
	hyde publish

travis:
	./push.sh

