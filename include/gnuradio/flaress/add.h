/* -*- c++ -*- */
/*
 * Copyright 2004,2009,2012,2018 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */


#ifndef ADD_H
#define ADD_H

#include <gnuradio/flaress/api.h>
#include <gnuradio/sync_block.h>
#include <cstdint>

namespace gr {
namespace flaress {

/*!
 * \brief output = sum(input[0], input[1], ..., input[M-1])
 * \ingroup math_operators_blk
 *
 * \details
 * Add samples across all input streams. For all \f$n\f$ samples
 * on all \f$M\f$ input streams \f$x_m\f$:
 *
 * \f[
 *   y[n] = \sum_{m=0}^{M-1} x_m[n]
 * \f]
 */
template <class T>
class FLARESS_API add : virtual public sync_block
{
public:
    // gr::blocks::add::sptr
    typedef std::shared_ptr<add<T>> sptr;

    static sptr make(size_t vlen = 1);
};

typedef add<double> add_double;
typedef add<int64_t> add_int64;
} /* namespace flaress */
} /* namespace gr */

#endif /* ADD_H */