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
 
#ifndef INCLUDED_FLARESS_FIXED_POINT_MATH_FF_H
#define INCLUDED_FLARESS_FIXED_POINT_MATH_FF_H

#include <flaress/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace flaress {

  /*!
    * \brief Convert stream of floats to a limited stream of floats.
    * \ingroup flaress
     *
     */
    class FLARESS_API fixed_point_math_ff : virtual public gr::sync_block
    {
     public:
      typedef std::shared_ptr<fixed_point_math_ff> sptr;

    /*!
       * Convert stream of floats to a limited stream of floats in fixed point math,
       * depending on the number of bits.
       *
       * \param vlen vector length of data streams.
       * \param N_int number of bits used to represent the integer part.
       * \param N_frac number of bits used to represent the fractional part.
       */
      static sptr make(size_t vlen, int N_int, int N_frac);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_FIXED_POINT_MATH_FF_H */

