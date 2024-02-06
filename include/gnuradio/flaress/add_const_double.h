/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013,2018 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_FLARESS_ADD_CONST_DOUBLE_H
#define INCLUDED_FLARESS_ADD_CONST_DOUBLE_H

#include <gnuradio/flaress/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace flaress {

  /*!
     * \brief output = input + constant
     * \ingroup math_operators_blk
     */
  class FLARESS_API add_const_double : virtual public gr::sync_block
  {
  public:
    typedef std::shared_ptr<add_const_double> sptr;

    /*!
       * \brief Create an instance of add_const_double
       * \param k additive constant
       */
    static sptr make(double k, size_t vlen);

    /*!
       * \brief Set additive constant
       */
    virtual void set_k(double k) = 0;
  };

  } // namespace flaress
  } // namespace gr

#endif /* INCLUDED_FLARESS_ADD_CONT_DOUBLE_H */

