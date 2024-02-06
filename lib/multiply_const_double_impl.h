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
#ifndef INCLUDED_FLARESS_MULTIPLY_CONST_DOUBLE_IMPL_H
#define INCLUDED_FLARESS_MULTIPLY_CONST_DOUBLE_IMPL_H

#include <gnuradio/flaress/multiply_const_double.h>

namespace gr {
  namespace flaress {

    class multiply_const_double_impl : public multiply_const_double
    {
      double d_k;
      size_t d_vlen;

     public:
       multiply_const_double_impl(double k, size_t vlen);
       ~multiply_const_double_impl();

       void set_k(double k) { d_k = k; }

       // Where all the action really happens
       int work(int noutput_items,
                gr_vector_const_void_star &input_items,
                gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_MULTIPLY_CONST_DOUBLE_IMPL_H */

