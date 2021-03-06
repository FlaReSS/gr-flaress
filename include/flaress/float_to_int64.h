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


#ifndef INCLUDED_FLARESS_FLOAT_TO_INT64_H
#define INCLUDED_FLARESS_FLOAT_TO_INT64_H

#include <flaress/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace flaress {

    /*!
    * \brief Convert stream of floats to a stream of ints.
    * \ingroup type_converters_blks
     *
     */
    class FLARESS_API float_to_int64 : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<float_to_int64> sptr;

      /*!
       * Build a float to int64 block.
       *
       * \param vlen vector length of data streams.
       * \param scale a scalar multiplier to change the output signal scale.
       */
      static sptr make(size_t vlen=1, double scale=1.0);

      /*!
       * Get the scalar multiplier value.
       */
      virtual double scale() const = 0;

      /*!
       * Set the scalar multiplier value.
       */
      virtual void set_scale(double scale) = 0;
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_FLOAT_TO_INT64_H */
