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
/* BINDTOOL_HEADER_FILE(sub_int64.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(3fff22e9979c00e54df14c2714bca5a6)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/flaress/sub_int64.h>
// pydoc.h is automatically generated in the build directory
#include <sub_int64_pydoc.h>

void bind_sub_int64(py::module& m)
{

    using sub_int64    = ::gr::flaress::sub_int64;


    py::class_<sub_int64, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<sub_int64>>(m, "sub_int64", D(sub_int64))

        .def(py::init(&sub_int64::make),
           py::arg("vlen"),
           D(sub_int64,make)
        )
        



        ;




}







