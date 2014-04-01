all:
	hyde gen

force:
	hyde gen -r

publish:
	hyde gen -r
	hyde publish
