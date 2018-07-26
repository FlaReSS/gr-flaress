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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "float_to_int64_impl.h"
#include "float_array_to_int64.h"

namespace gr {
  namespace flaress {

    float_to_int64::sptr
    float_to_int64::make(size_t vlen, double scale)
    {
      return gnuradio::get_initial_sptr
        (new float_to_int64_impl(vlen, scale));
    }

    float_to_int64_impl::float_to_int64_impl(size_t vlen, double scale)
      : gr::sync_block("float_to_int64",
              gr::io_signature::make(1, 1,sizeof(float)*vlen),
              gr::io_signature::make(1, 1, sizeof(int64_t)*vlen)),
              d_vlen(vlen), d_scale(scale)
    {}

    float_to_int64_impl::~float_to_int64_impl()
    {
    }

    int
    float_to_int64_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      int64_t *out = (int64_t *) output_items[0];

      float_array_to_int64 (in, out, d_scale, d_vlen*noutput_items);

      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */
