#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/isispace/gnuradio/gr-flaress/python
export PATH=/home/isispace/gnuradio/gr-flaress/build/python:$PATH
export LD_LIBRARY_PATH=/home/isispace/gnuradio/gr-flaress/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/isispace/gnuradio/gr-flaress/build/swig:$PYTHONPATH
/usr/bin/python2 /home/isispace/gnuradio/gr-flaress/python/qa_snr_estimator.py 
