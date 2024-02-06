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
/* BINDTOOL_HEADER_FILE(debug_func_probe.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(696a3e4aa7e26f6e2cc17239b14c8a02)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <flaress/debug_func_probe.h>
// pydoc.h is automatically generated in the build directory
#include <debug_func_probe_pydoc.h>

void bind_debug_func_probe(py::module& m)
{

    using debug_func_probe    = ::gr::flaress::debug_func_probe;


    py::class_<debug_func_probe, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<debug_func_probe>>(m, "debug_func_probe", D(debug_func_probe))

        .def(py::init(&debug_func_probe::make),
           py::arg("sizeof_stream_item"),
           D(debug_func_probe,make)
        )
        




        
        .def("reset",&debug_func_probe::reset,       
            D(debug_func_probe,reset)
        )


        
        .def("debug_nitems",&debug_func_probe::debug_nitems,       
            D(debug_func_probe,debug_nitems)
        )


        
        .def("data",&debug_func_probe::data,       
            D(debug_func_probe,data)
        )

        ;




}








