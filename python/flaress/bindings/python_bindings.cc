/*
 * Copyright 2020 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include <pybind11/pybind11.h>

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/arrayobject.h>

namespace py = pybind11;

// Headers for binding functions
/**************************************/
// The following comment block is used for
// gr_modtool to insert function prototypes
// Please do not delete
/**************************************/
// BINDING_FUNCTION_PROTOTYPES(

void bind_add_const_double(py::module&);
void bind_add_const_int64(py::module&);
void bind_add_double(py::module&);
void bind_add_int64(py::module&);
void bind_debug_func_probe(py::module&);
void bind_divide_double(py::module&);
void bind_divide_int64(py::module&);
void bind_fixed_point_math_cc(py::module&);
void bind_fixed_point_math_dd(py::module&);
void bind_fixed_point_math_ff(py::module&);
void bind_float_to_double(py::module&);
void bind_float_to_int64(py::module&);
void bind_integer_math_ii(py::module&);
void bind_integer_math_ll(py::module&);
void bind_int_to_int64(py::module&);
void bind_multiply_const_double(py::module&);
void bind_multiply_const_int64(py::module&);
void bind_multiply_double(py::module&);
void bind_multiply_int64(py::module&);
void bind_null_sink(py::module&);
void bind_null_source(py::module&);
void bind_snr(py::module&);
void bind_sub_double(py::module&);
void bind_sub_int64(py::module&);
void bind_vector_sink_double(py::module&);
void bind_vector_sink_int64(py::module&);
void bind_vector_source_double(py::module&);
void bind_vector_source_int64(py::module&);

// ) END BINDING_FUNCTION_PROTOTYPES


// We need this hack because import_array() returns NULL
// for newer Python versions.
// This function is also necessary because it ensures access to the C API
// and removes a warning.
void* init_numpy()
{
    import_array();
    return NULL;
}

PYBIND11_MODULE(flaress_python, m)
{
    // Initialize the numpy C API
    // (otherwise we will see segmentation faults)
    init_numpy();

    // Allow access to base block methods
    py::module::import("gnuradio.gr");

    /**************************************/
    // The following comment block is used for
    // gr_modtool to insert binding function calls
    // Please do not delete
    /**************************************/
    // BINDING_FUNCTION_CALLS(

    bind_add_const_double(m);
    bind_add_const_int64(m);
    bind_add_double(m);
    bind_add_int64(m);
    bind_debug_func_probe(m);
    bind_divide_double(m);
    bind_divide_int64(m);
    bind_fixed_point_math_cc(m);
    bind_fixed_point_math_dd(m);
    bind_fixed_point_math_ff(m);
    bind_float_to_double(m);
    bind_float_to_int64(m);
    bind_integer_math_ii(m);
    bind_integer_math_ll(m);
    bind_int_to_int64(m);
    bind_multiply_const_double(m);
    bind_multiply_const_int64(m);
    bind_multiply_double(m);
    bind_multiply_int64(m);
    bind_null_sink(m);
    bind_null_source(m);
    bind_snr(m);
    bind_sub_double(m);
    bind_sub_int64(m);
    bind_vector_sink_double(m);
    bind_vector_sink_int64(m);
    bind_vector_source_double(m);
    bind_vector_source_int64(m);

    // ) END BINDING_FUNCTION_CALLS
}
