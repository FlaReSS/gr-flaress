/* -*- c++ -*- */

#define FLARESS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "flaress_swig_doc.i"

%{
#include "flaress/float_to_double.h"
#include "flaress/float_to_int64.h"
#include "flaress/selector.h"
#include "flaress/snr.h"
%}

%constant int sizeof_long = sizeof(int64_t);

%include "flaress/float_to_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, float_to_double);
%include "flaress/float_to_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, float_to_int64);
%include "flaress/selector.h"
GR_SWIG_BLOCK_MAGIC2(flaress, selector);
%include "flaress/snr.h"
GR_SWIG_BLOCK_MAGIC2(flaress, snr);
