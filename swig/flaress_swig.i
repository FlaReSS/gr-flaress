/* -*- c++ -*- */

#define FLARESS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "flaress_swig_doc.i"

%{
#include "flaress/selector_cc.h"
#include "flaress/selector_ff.h"
#include "flaress/float_to_double.h"
%}


%include "flaress/selector_cc.h"
GR_SWIG_BLOCK_MAGIC2(flaress, selector_cc);
%include "flaress/selector_ff.h"
GR_SWIG_BLOCK_MAGIC2(flaress, selector_ff);
%include "flaress/float_to_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, float_to_double);
