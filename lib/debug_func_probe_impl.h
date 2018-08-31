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

#ifndef INCLUDED_FLARESS_DEBUG_FUNC_PROBE_IMPL_H
#define INCLUDED_FLARESS_DEBUG_FUNC_PROBE_IMPL_H

#include <flaress/debug_func_probe.h>

namespace gr {
  namespace flaress {

    class debug_func_probe_impl : public debug_func_probe
    {
     private:
       std::vector<long int> d_data;

     public:
      debug_func_probe_impl(size_t sizeof_stream_item);
      ~debug_func_probe_impl();

      void debug_nitems();
      void reset();
      std::vector<long int> data() const;

      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_DEBUG_FUNC_PROBE_IMPL_H */
