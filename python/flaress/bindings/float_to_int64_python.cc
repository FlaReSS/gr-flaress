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
/* BINDTOOL_HEADER_FILE(float_to_int64.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(8e3259ea885a603d353d31b35b05c0d0)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/flaress/float_to_int64.h>
// pydoc.h is automatically generated in the build directory
#include <float_to_int64_pydoc.h>

void bind_float_to_int64(py::module& m)
{

    using float_to_int64    = ::gr::flaress::float_to_int64;


    py::class_<float_to_int64, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<float_to_int64>>(m, "float_to_int64", D(float_to_int64))

        .def(py::init(&float_to_int64::make),
           py::arg("vlen") = 1,
           py::arg("scale") = 1.,
           D(float_to_int64,make)
        )
        




        
        .def("scale",&float_to_int64::scale,       
            D(float_to_int64,scale)
        )


        
        .def("set_scale",&float_to_int64::set_scale,       
            py::arg("scale"),
            D(float_to_int64,set_scale)
        )

        ;




}







