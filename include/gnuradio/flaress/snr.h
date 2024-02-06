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


#ifndef INCLUDED_FLARESS_SNR_H
#define INCLUDED_FLARESS_SNR_H

#include <gnuradio/flaress/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace flaress {

    /*!
     * \brief <+description of block+>
     * \ingroup flaress
     *
     */
    class FLARESS_API snr : virtual public gr::sync_block
    {
     public:
      typedef std::shared_ptr<snr> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of flaress::snr.
       *
       * To avoid accidental use of raw pointers, flaress::snr's
       * constructor is in a private implementation
       * class. flaress::snr::make is the public interface for
       * creating new instances.
       */
      static sptr make(bool auto_carrier, bool carrier, bool all_spectrum, float freq_central, float samp_rate, int nintems, float signal_bw, float noise_bw);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_SNR_H */
