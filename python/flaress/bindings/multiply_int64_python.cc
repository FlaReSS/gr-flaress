/*
 * Copyright 2024 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(multiply_int64.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(700a19f2b2e5f6833d2a3f9c4513324b)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/flaress/multiply_int64.h>
// pydoc.h is automatically generated in the build directory
#include <multiply_int64_pydoc.h>

void bind_multiply_int64(py::module& m)
{

    using multiply_int64    = ::gr::flaress::multiply_int64;


    py::class_<multiply_int64, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<multiply_int64>>(m, "multiply_int64", D(multiply_int64))

        .def(py::init(&multiply_int64::make),
           py::arg("vlen") = 1,
           D(multiply_int64,make)
        )
        



        ;




}








