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

#ifndef INCLUDED_FLARESS_VECTOR_SOURCE_DOUBLE_IMPL_H
#define INCLUDED_FLARESS_VECTOR_SOURCE_DOUBLE_IMPL_H

#include <gnuradio/flaress/vector_source_double.h>

namespace gr {
  namespace flaress {

    class vector_source_double_impl : public vector_source_double
    {
      private:
        std::vector<double> d_data;
        bool d_repeat;
        unsigned int d_offset;
        int d_vlen;
        bool d_settags;
        std::vector<tag_t> d_tags;
        unsigned int d_tagpos;

      public:
        vector_source_double_impl(const std::vector<double> &data,
                                  bool repeat, int vlen,
                                  const std::vector<tag_t> &tags);
        ~vector_source_double_impl();

        void rewind() { d_offset = 0; }
        void set_data(const std::vector<double> &data,
                      const std::vector<tag_t> &tags);
        void set_repeat(bool repeat) { d_repeat = repeat; };

        int work(int noutput_items,
                 gr_vector_const_void_star &input_items,
                 gr_vector_void_star &output_items);
      };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_VECTOR_SOURCE_DOUBLE_IMPL_H */

