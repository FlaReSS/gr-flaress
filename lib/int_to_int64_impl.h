/* -*- c++ -*- */
/*
 * Copyright 2011-2012 Free Software Foundation, Inc.
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

#ifndef INCLUDED_FLARESS_INT_TO_INT64_IMPL_H
#define INCLUDED_FLARESS_INT_TO_INT64_IMPL_H

#include <flaress/int_to_int64.h>

    namespace gr {
  namespace flaress {

  class int_to_int64_impl : public int_to_int64
  {
  private:
    size_t d_vlen;
    int d_scale;

  public:
    int_to_int64_impl(size_t vlen, int scale);
    ~int_to_int64_impl();

    virtual int scale() const { return d_scale; }
    virtual void set_scale(int scale) { d_scale = scale; }

    // Where all the action really happens
    int work(int noutput_items,
             gr_vector_const_void_star &input_items,
             gr_vector_void_star &output_items);
  };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_INT_TO_INT64_IMPL_H */

