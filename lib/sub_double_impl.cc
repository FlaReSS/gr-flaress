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
#include "sub_double_impl.h"

namespace gr {
  namespace flaress {

    sub_double::sptr
    sub_double::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new sub_double_impl(vlen));
    }

    /*
     * The private constructor
     */
    sub_double_impl::sub_double_impl(size_t vlen)
        : gr::sync_block("sub_double",
                         io_signature::make(2, 2, sizeof(double) * vlen),
                         io_signature::make(1, 1, sizeof(double) * vlen)),
          d_vlen(vlen)
    {}

    /*
     * Our virtual destructor.
     */
    sub_double_impl::~sub_double_impl()
    {
    }

    int
    sub_double_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      double *out = (double *)output_items[0];
      double *in1 = (double *)input_items[0];
      double *in2 = (double *)input_items[1];

      for (size_t i = 1; i < input_items.size(); i++)
      {
        double *in = (double *)input_items[i];
        for (int j = 0; j < noutput_items * d_vlen; j++)
        {
          out[j] = in1[j] - in2[j];
        }
      }

      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */

