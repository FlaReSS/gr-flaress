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
#include "snr_impl.h"

namespace gr {
  namespace flaress {

    snr::sptr
    snr::make(bool carrier, int samp_rate, int nintems, float signal_bw, float noise_bw)
    {
      return gnuradio::get_initial_sptr
        (new snr_impl(carrier, samp_rate, nintems, signal_bw, noise_bw));
    }

    /*
     * The private constructor
     */
    snr_impl::snr_impl(bool carrier, int samp_rate, int nintems, float signal_bw, float noise_bw)
      : gr::sync_block("snr",
              gr::io_signature::make(1, 1, sizeof(float) * nintems),
              gr::io_signature::make(1, 1, sizeof(float))),
              d_nintems_half(nintems / 2), d_nintems(nintems),
              d_samp_rate(samp_rate), d_carrier(carrier),
              signal_item_offset((signal_bw / samp_rate) * (nintems / 4)),
              noise_item_offset((noise_bw / samp_rate) * (nintems / 4))
    {}

    /*
     * Our virtual destructor.
     */
    snr_impl::~snr_impl()
    {}

    int
    snr_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      float window[d_nintems];
      int signal_item = 0;
      int signal_tot_items = 1;
      int noise_tot_items = 1;
      float signal_spectrum = -1000;
      float noise_spectrum_avg = 0;
      int j = 0;
      int debug = 0;

      for(int i = 0; i < (noutput_items * d_nintems ); i++) {
        if (j < d_nintems_half) {
          if (in [i] > signal_spectrum ) {
            signal_spectrum = in [i];
            signal_item = j;
          }
          window[j + d_nintems_half] = in [i];
        }

        if (j >= d_nintems_half && j < d_nintems) {
          if (in [i] > signal_spectrum ) {
            signal_spectrum = in [i];
            signal_item = j;
          }
          window[j - d_nintems_half] = in [i];
        }

        j ++;
        if(j == d_nintems ){

          if (d_carrier == false) {
            signal_spectrum = 0;
          }

          for (size_t w = 0; w < d_nintems; w++) {
            if (((w >= (signal_item - noise_item_offset)) && (w < (signal_item - signal_item_offset))) || ((w > (signal_item + signal_item_offset)) && (w <= (signal_item + noise_item_offset)))) {
                 noise_spectrum_avg += window[w];
                 noise_tot_items ++;
            }
            if ((w < signal_item - signal_item_offset ) || (w > signal_item + signal_item_offset )) {
                 if (d_carrier == false) {
                   signal_spectrum += window[w];
                   signal_tot_items ++;
                 }
            }
          }

          *out++ = (signal_spectrum / signal_tot_items) - (noise_spectrum_avg / noise_tot_items);
          j = 0;
        }
      }




        // out[i] = (signal_spectrum / signal_tot_items) - (noise_spectrum_avg / noise_tot_items);


      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace flaress */
} /* namespace gr */
