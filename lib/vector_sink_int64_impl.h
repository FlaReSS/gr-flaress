/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013,2017-2018 Free Software Foundation, Inc.
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

#ifndef INCLUDED_FLARESS_VECTOR_SINK_INT64_IMPL_H
#define INCLUDED_FLARESS_VECTOR_SINK_INT64_IMPL_H

#include <flaress/vector_sink_int64.h>

namespace gr {
  namespace flaress {

    class vector_sink_int64_impl : public vector_sink_int64
    {
    private:
      std::vector<int64_t> d_data;
      std::vector<tag_t> d_tags;
      mutable gr::thread::mutex d_data_mutex; // protects internal data access.
      int d_vlen;

    public:
      vector_sink_int64_impl(const int vlen, const int reserve_items);
      ~vector_sink_int64_impl();

      void reset();
      std::vector<long int> data() const;
      std::vector<tag_t> tags() const;

      int work(int noutput_items,
               gr_vector_const_void_star &input_items,
               gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_VECTOR_SINK_INT64_IMPL_H */
