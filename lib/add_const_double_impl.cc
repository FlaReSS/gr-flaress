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
#include "add_const_double_impl.h"
#include <volk/volk.h>

namespace gr {
  namespace flaress {

    add_const_double::sptr
    add_const_double::make(double k, size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new add_const_double_impl(k, vlen));
    }

    /*
     * The private constructor
     */
    add_const_double_impl::add_const_double_impl(double k, size_t vlen)
        : gr::sync_block("add_const_double",
                         io_signature::make(1, 1, sizeof(double) *vlen),
                         io_signature::make(1, 1, sizeof(double) *vlen)),
          d_k(k), d_vlen(vlen)
    {
      const int alignment_multiple =
          volk_get_alignment() / sizeof(double);
      set_alignment(std::max(1, alignment_multiple));
    }

    /*
     * Our virtual destructor.
     */
    add_const_double_impl::~add_const_double_impl()
    {
    }

    int
    add_const_double_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const double *in = (const double *)input_items[0];
      double *out = (double *)output_items[0];

      for (int j = 0; j < (noutput_items * d_vlen); j++)
      {
        out[j] = in[j] + d_k;
        }
      

      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */

