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
 
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "integer_math_ii_impl.h"

namespace gr {
  namespace flaress {

    integer_math_ii::sptr
    integer_math_ii::make(size_t vlen, int N_int)
    {
      return gnuradio::get_initial_sptr
        (new integer_math_ii_impl(vlen, N_int));
    }

    integer_math_ii_impl::integer_math_ii_impl(size_t vlen, int N_int)
      : gr::sync_block("integer_math_ii",
              gr::io_signature::make(1, 1, sizeof(int)*vlen),
              gr::io_signature::make(1, 1, sizeof(int)*vlen)),
              d_vlen(vlen), d_N_int(N_int)
    {
      if(d_N_int > 32) {
        throw std::out_of_range ("fixed_point_math: the maximum total number of bits cannot be greater of 32 bits.");
      }
      
      if(d_N_int < 0) {
        throw std::out_of_range ("fixed_point_math: the number of bits cannot be negatives.");
      }

      max_value_pos = (pow(2,(d_N_int - 1)) - 1);
      max_value_neg = -pow(2,(d_N_int - 1));
    }

    integer_math_ii_impl::~integer_math_ii_impl()
    {}

    int
    integer_math_ii_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const int *in = (const int *) input_items[0];
      int *out = (int *) output_items[0];

      for(size_t i = 0; i < (noutput_items * d_vlen); i++)
      {
        if(rounded > max_value_pos){
          rounded = max_value_pos;
        }
        if(rounded < max_value_neg){
          rounded = max_value_neg;
        }

        out[i]= rounded;
      }

      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */

