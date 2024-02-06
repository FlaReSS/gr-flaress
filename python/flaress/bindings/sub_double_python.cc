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
/* BINDTOOL_HEADER_FILE(sub_double.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(70c5703ea66217378b15228fce65e48b)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/flaress/sub_double.h>
// pydoc.h is automatically generated in the build directory
#include <sub_double_pydoc.h>

void bind_sub_double(py::module& m)
{

    using sub_double    = ::gr::flaress::sub_double;


    py::class_<sub_double, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<sub_double>>(m, "sub_double", D(sub_double))

        .def(py::init(&sub_double::make),
           py::arg("vlen"),
           D(sub_double,make)
        )
        



        ;




}








