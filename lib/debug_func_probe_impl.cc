/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013,2018 Free Software Foundation, Inc.
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
#include "debug_func_probe_impl.h"

namespace gr {
  namespace flaress {

    debug_func_probe::sptr
    debug_func_probe::make(size_t sizeof_stream_item)
    {
      return gnuradio::get_initial_sptr
        (new debug_func_probe_impl(sizeof_stream_item));
    }

    /*
     * The private constructor
     */
    debug_func_probe_impl::debug_func_probe_impl(size_t sizeof_stream_item)
      : gr::sync_block("debug_func_probe",
              gr::io_signature::make(1, 1, sizeof_stream_item),
              gr::io_signature::make(0, 0, 0))
    {
      reset();
    }

    debug_func_probe_impl::~debug_func_probe_impl()
    {}

    int
    debug_func_probe_impl::work(int noutput_items,
                         gr_vector_const_void_star &input_items,
                         gr_vector_void_star &output_items)
    {
      return noutput_items;
    }

    void
    debug_func_probe_impl::debug_nitems()
    {
        d_data.push_back((long int) nitems_read(0));
    }

    std::vector<long int>
    debug_func_probe_impl::data() const
    {
      return d_data;
    }

    void
    debug_func_probe_impl::reset()
    {
      d_data.clear();
    }

  } /* namespace flaress */
} /* namespace gr */
