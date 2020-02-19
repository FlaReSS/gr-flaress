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
#include "add_int64_impl.h"

namespace gr {
  namespace flaress {

    add_int64::sptr
    add_int64::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new add_int64_impl(vlen));
    }

    /*
     * The private constructor
     */
    add_int64_impl::add_int64_impl(size_t vlen)
        : gr::sync_block("add_int64",
                         io_signature::make(1, -1, sizeof(int64_t) * vlen),
                         io_signature::make(1, 1, sizeof(int64_t) * vlen)),
          d_vlen(vlen)
    {
    }

    /*
     * Our virtual destructor.
     */
    add_int64_impl::~add_int64_impl()
    {
    }

    int
    add_int64_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      int64_t *out = (int64_t *)output_items[0];
      int noi = d_vlen * noutput_items;

      for (size_t i = 1; i < input_items.size(); i++)
      {
        int64_t *in = (int64_t *)input_items[i];
        for (int j = 0; j < noutput_items * d_vlen; j++)
        {
          out[j] = out[j] + in[j];
        }
      }

      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */

