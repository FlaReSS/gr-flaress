/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2012-2013 Free Software Foundation, Inc.
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


#ifndef INCLUDED_FLARESS_VECTOR_SOURCE_INT64_IMPL_H
#define INCLUDED_FLARESS_VECTOR_SOURCE_INT64_IMPL_H

#include <flaress/vector_source_int64.h>

    namespace gr {
  namespace flaress {

    class vector_source_int64_impl : public vector_source_int64
    {
      private:
        std::vector<long int> d_data;
        bool d_repeat;
        unsigned int d_offset;
        int d_vlen;
        bool d_settags;
        std::vector<tag_t> d_tags;
        unsigned int d_tagpos;  

    public:
      vector_source_int64_impl(const std::vector<long int> &data, bool repeat, int vlen, const std::vector<tag_t> &tags);
      ~vector_source_int64_impl();

      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);

      void rewind() { d_offset = 0; }
      void set_data(const std::vector<long int> &data,
                    const std::vector<tag_t> &tags);
      void set_repeat(bool repeat) { d_repeat = repeat; };
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_VECTOR_SOURCE_INT64_IMPL_H */

