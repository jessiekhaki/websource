all:
	hyde gen

force:
	hyde gen -r

publish:
	hyde gen -r
	hyde publish

travis:
	cd ..
	git clone git@github.com:chicas-lancaster/chicas-lancaster.github.io.git
	cd websource
	hyde gen -r
	hyde publish
