/* -*- c++ -*- */
/*
 * Copyright 2004,2009,2012,2018 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */


#ifndef ADD_IMPL_H
#define ADD_IMPL_H

#include <gnuradio/flaress/add.h>

namespace gr {
namespace flaress {

template <class T>
class FLARESS_API add_impl : public add<T>
{
private:
    const size_t d_vlen;

public:
    add_impl(size_t vlen);

    int work(int noutput_items,
             gr_vector_const_void_star& input_items,
             gr_vector_void_star& output_items) override;
};

} /* namespace flaress */
} /* namespace gr */

#endif /* ADD_IMPL_H */