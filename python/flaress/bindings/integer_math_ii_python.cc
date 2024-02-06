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
/* BINDTOOL_HEADER_FILE(integer_math_ii.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(8f541e002c78140fb139668db92871c4)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <flaress/integer_math_ii.h>
// pydoc.h is automatically generated in the build directory
#include <integer_math_ii_pydoc.h>

void bind_integer_math_ii(py::module& m)
{

    using integer_math_ii    = ::gr::flaress::integer_math_ii;


    py::class_<integer_math_ii, gr::sync_block, gr::block, gr::basic_block,
        std::shared_ptr<integer_math_ii>>(m, "integer_math_ii", D(integer_math_ii))

        .def(py::init(&integer_math_ii::make),
           py::arg("vlen"),
           py::arg("N_int"),
           D(integer_math_ii,make)
        )
        



        ;




}








