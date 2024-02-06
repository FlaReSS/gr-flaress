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
/* BINDTOOL_HEADER_FILE(null_source.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(81952c339426f9da7b6092123f3da6bd)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <flaress/null_source.h>
// pydoc.h is automatically generated in the build directory
#include <null_source_pydoc.h>

void bind_null_source(py::module& m)
{

    using null_source    = ::gr::flaress::null_source;


    py::class_<null_source, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<null_source>>(m, "null_source", D(null_source))

        .def(py::init(&null_source::make),
           py::arg("sizeof_stream_item"),
           D(null_source,make)
        )
        



        ;




}








