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

#ifndef INCLUDED_FLARESS_FLOAT_TO_INT64_IMPL_H
#define INCLUDED_FLARESS_FLOAT_TO_INT64_IMPL_H

#include <flaress/float_to_int64.h>

namespace gr {
  namespace flaress {

    class float_to_int64_impl : public float_to_int64
    {
     private:
       size_t d_vlen;
       double d_scale;

     public:
      float_to_int64_impl(size_t vlen, double scale);
      ~float_to_int64_impl();

      virtual double scale() const { return d_scale; }
      virtual void set_scale(double scale) { d_scale = scale; }

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_FLOAT_TO_INT64_IMPL_H */
