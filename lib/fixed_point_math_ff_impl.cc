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
#include "fixed_point_math_ff_impl.h"

namespace gr {
  namespace flaress {

    fixed_point_math_ff::sptr
    fixed_point_math_ff::make(size_t vlen, int N_int, int N_frac)
    {
      return gnuradio::get_initial_sptr
        (new fixed_point_math_ff_impl(vlen, N_int, N_frac));
    }

    fixed_point_math_ff_impl::fixed_point_math_ff_impl(size_t vlen, int N_int, int N_frac)
      : gr::sync_block("fixed_point_math_ff",
              gr::io_signature::make(1, 1, sizeof(float)*vlen),
              gr::io_signature::make(1, 1, sizeof(float)*vlen)),
              d_vlen(vlen), d_N_int(N_int), d_N_frac(N_frac)
    {
      if((d_N_int + d_N_frac) > 64) {
        throw std::out_of_range ("fixed_point_math: the maximum total number of bits cannot be greater of 64 bits.");
      }
      
      if(d_N_int < 0 || d_N_frac < 0) {
        throw std::out_of_range ("fixed_point_math: the number of bits cannot be negatives.");
      }

      min_frac = pow(2,(- (d_N_frac)));
      max_value_pos = (pow(2,(d_N_int - 1)) - 1) + (1 - min_frac);
      max_value_neg = -pow(2,(d_N_int - 1));
    }

    fixed_point_math_ff_impl::~fixed_point_math_ff_impl()
    {}

    int
    fixed_point_math_ff_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      for(size_t i = 0; i < (noutput_items * d_vlen); i++)
      {
        int64_t rounded_temp = (int64_t) (in[i] / min_frac);
        float rounded = rounded_temp * min_frac;
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

