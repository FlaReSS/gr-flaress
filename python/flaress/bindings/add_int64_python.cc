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
/* BINDTOOL_HEADER_FILE(add_int64.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(c6dc7edecfad13b7f09d9187d53298c2)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/flaress/add_int64.h>
// pydoc.h is automatically generated in the build directory
#include <add_int64_pydoc.h>

void bind_add_int64(py::module& m)
{

    using add_int64    = ::gr::flaress::add_int64;


    py::class_<add_int64, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<add_int64>>(m, "add_int64", D(add_int64))

        .def(py::init(&add_int64::make),
           py::arg("vlen") = 1,
           D(add_int64,make)
        )
        



        ;




}







