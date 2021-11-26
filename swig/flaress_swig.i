/* -*- c++ -*- */

#define FLARESS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "flaress_swig_doc.i"

%{
#include "flaress/float_to_double.h"
#include "flaress/float_to_int64.h"
#include "flaress/snr.h"
#include "flaress/vector_sink_int64.h"
#include "flaress/vector_sink_double.h"
#include "flaress/null_sink.h"
#include "flaress/debug_func_probe.h"
#include "flaress/null_source.h"
#include "flaress/vector_source_double.h"
#include "flaress/vector_source_int64.h"
#include "flaress/int_to_int64.h"
#include "flaress/fixed_point_math_cc.h"
#include "flaress/fixed_point_math_ff.h"
#include "flaress/fixed_point_math_dd.h"
#include "flaress/integer_math_ii.h"
#include "flaress/integer_math_ll.h"
#include "flaress/multiply_double.h"
#include "flaress/multiply_int64.h"
#include "flaress/multiply_const_double.h"
#include "flaress/multiply_const_int64.h"
#include "flaress/add_double.h"
#include "flaress/add_const_double.h"
#include "flaress/add_int64.h"
#include "flaress/add_const_int64.h"
#include "flaress/sub_int64.h"
#include "flaress/sub_double.h"
#include "flaress/divide_double.h"
#include "flaress/divide_int64.h"
%}

%constant int sizeof_long = sizeof(int64_t);

%include "flaress/float_to_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, float_to_double);
%include "flaress/float_to_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, float_to_int64);
%include "flaress/snr.h"
GR_SWIG_BLOCK_MAGIC2(flaress, snr);
%include "flaress/vector_sink_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, vector_sink_int64);
%include "flaress/vector_sink_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, vector_sink_double);
%include "flaress/null_sink.h"
GR_SWIG_BLOCK_MAGIC2(flaress, null_sink);
%include "flaress/debug_func_probe.h"
GR_SWIG_BLOCK_MAGIC2(flaress, debug_func_probe);
%include "flaress/null_source.h"
GR_SWIG_BLOCK_MAGIC2(flaress, null_source);
%include "flaress/vector_source_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, vector_source_double);
%include "flaress/vector_source_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, vector_source_int64);
%include "flaress/int_to_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, int_to_int64);

%include "flaress/fixed_point_math_cc.h"
GR_SWIG_BLOCK_MAGIC2(flaress, fixed_point_math_cc);
%include "flaress/fixed_point_math_ff.h"
GR_SWIG_BLOCK_MAGIC2(flaress, fixed_point_math_ff);
%include "flaress/fixed_point_math_dd.h"
GR_SWIG_BLOCK_MAGIC2(flaress, fixed_point_math_dd);
%include "flaress/integer_math_ii.h"
GR_SWIG_BLOCK_MAGIC2(flaress, integer_math_ii);
%include "flaress/integer_math_ll.h"
GR_SWIG_BLOCK_MAGIC2(flaress, integer_math_ll);

%include "flaress/multiply_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, multiply_double);
%include "flaress/multiply_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, multiply_int64);
%include "flaress/multiply_const_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, multiply_const_double);
%include "flaress/multiply_const_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, multiply_const_int64);
%include "flaress/add_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, add_double);
%include "flaress/add_const_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, add_const_double);
%include "flaress/add_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, add_int64);
%include "flaress/add_const_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, add_const_int64);
%include "flaress/sub_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, sub_int64);
%include "flaress/sub_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, sub_double);
%include "flaress/divide_double.h"
GR_SWIG_BLOCK_MAGIC2(flaress, divide_double);
%include "flaress/divide_int64.h"
GR_SWIG_BLOCK_MAGIC2(flaress, divide_int64);
