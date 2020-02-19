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
#include "add_double_impl.h"
#include <volk/volk.h>

namespace gr {
  namespace flaress {

    add_double::sptr
    add_double::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new add_double_impl(vlen));
    }

    /*
     * The private constructor
     */
    add_double_impl::add_double_impl(size_t vlen)
        : gr::sync_block("add_double",
                         io_signature::make(1, -1, sizeof(double) * vlen),
                         io_signature::make(1, 1, sizeof(double) * vlen)),
          d_vlen(vlen)
    {
      const int alignment_multiple =
          volk_get_alignment() / sizeof(double);
      set_alignment(std::max(1, alignment_multiple));
    }

    /*
     * Our virtual destructor.
     */
    add_double_impl::~add_double_impl()
    {
    }

    int
    add_double_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      double *out = (double *)output_items[0];
      int noi = d_vlen * noutput_items;

      memcpy(out, input_items[0], noi * sizeof(double));
      for (size_t i = 1; i < input_items.size(); i++)
        volk_64f_x2_add_64f(out, out, (const double *)input_items[i], noi);
      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */

