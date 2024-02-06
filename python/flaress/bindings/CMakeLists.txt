# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT flaress_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT flaress_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND flaress_python_files
    add_const_double_python.cc
    add_const_int64_python.cc
    add_double_python.cc
    add_int64_python.cc
    debug_func_probe_python.cc
    divide_double_python.cc
    divide_int64_python.cc
    fixed_point_math_cc_python.cc
    fixed_point_math_dd_python.cc
    fixed_point_math_ff_python.cc
    float_to_double_python.cc
    float_to_int64_python.cc
    integer_math_ii_python.cc
    integer_math_ll_python.cc
    int_to_int64_python.cc
    multiply_const_double_python.cc
    multiply_const_int64_python.cc
    multiply_double_python.cc
    multiply_int64_python.cc
    null_sink_python.cc
    null_source_python.cc
    snr_python.cc
    sub_double_python.cc
    sub_int64_python.cc
    vector_sink_double_python.cc
    vector_sink_int64_python.cc
    vector_source_double_python.cc
    vector_source_int64_python.cc
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(flaress
   ../../..
   gr::flaress
   "${flaress_python_files}")

# copy in bindings .so file for use in QA test module
add_custom_target(
  copy_bindings_for_tests ALL
  COMMAND
    ${CMAKE_COMMAND} -E copy "${CMAKE_CURRENT_BINARY_DIR}/*.so"
    ${CMAKE_BINARY_DIR}/test_modules/gnuradio/flaress/
  DEPENDS flaress_python)

install(TARGETS flaress_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/flaress COMPONENT pythonapi)
