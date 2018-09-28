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

#ifndef INCLUDED_FLARESS_SNR_IMPL_H
#define INCLUDED_FLARESS_SNR_IMPL_H

#include <flaress/snr.h>

namespace gr {
  namespace flaress {

    class snr_impl : public snr
    {
     private:
      bool d_carrier;
      bool d_auto_carrier;
      float d_samp_rate;
      uint32_t d_freq_central_index;
      uint32_t d_nintems;
      uint32_t d_nintems_half;
      uint32_t signal_item_offset;
      uint32_t noise_item_offset;
      uint32_t noise_bw_items;
      uint32_t signal_bw_items;

      float *signal_band;
      float *noise_band;
      float *temp_buffer;
      float *fft_buffer;
      uint32_t *signal_max_index;
      float *signal_acc;
      float *noise_acc;

      void create_buffers();

          public : snr_impl(bool auto_carrier, bool carrier, float freq_central, float samp_rate, int nintems, float signal_bw, float noise_bw);
      ~snr_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_SNR_IMPL_H */
