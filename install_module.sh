#!/bin/bash
# Script to install a module in gnuradio.
#run it in the main folder of the OOT module

if [ $1 = '-make' ]; then
	source ~/prefix/setup_env.sh
	rm -r build
	mkdir build
	cd build
	cmake -DCMAKE_INSTALL_PREFIX=~/prefix ../
	make
elif [ $1 = '-test' ]; then
	source ~/prefix/setup_env.sh
	rm -r build
	mkdir build
	cd build
	cmake -DCMAKE_INSTALL_PREFIX=~/prefix ../
	make
	make test
elif [ $1 = '-complete' ]; then
	source ~/prefix/setup_env.sh
	rm -r build
	mkdir build
	cd build
	cmake -DCMAKE_INSTALL_PREFIX=~/prefix ../
	make
	make test
	make install
	ldconfig
else
	echo Please, specify between -make, -test, -complete
fi
