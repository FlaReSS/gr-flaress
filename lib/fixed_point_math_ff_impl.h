/* -*- c++ -*- */
/*
 * Copyright 2018 Antonio Miraglia - ISISpace.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */
#ifndef INCLUDED_FLARESS_FIXED_POINT_MATH_FF_IMPL_H
#define INCLUDED_FLARESS_FIXED_POINT_MATH_FF_IMPL_H

#include <gnuradio/flaress/fixed_point_math_ff.h>

namespace gr {
  namespace flaress {

    class fixed_point_math_ff_impl : public fixed_point_math_ff
    {
     private:
      size_t d_vlen;
      int d_N_int;
      int d_N_frac;
      float min_frac;
      float max_value_pos;
      float max_value_neg;

     public:
      fixed_point_math_ff_impl(size_t vlen, int N_int, int N_frac);
      ~fixed_point_math_ff_impl();

      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_FIXED_POINT_MATH_FF_IMPL_H */

