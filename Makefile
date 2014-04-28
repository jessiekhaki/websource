all:
	hyde gen

force:
	hyde gen -r

publish:
	hyde gen -r
	hyde publish

travis:
	echo "StrictHostKeyChecking no" >> ~/.ssh/config
	cd ..
	git clone git@github.com:chicas-lancaster/chicas-lancaster.github.io.git
	cd websource
	hyde gen -r
	hyde publish
