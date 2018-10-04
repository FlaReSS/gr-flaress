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
#include <volk/volk.h>

namespace gr {
  namespace flaress {

    snr::sptr
    snr::make(bool auto_carrier, bool carrier, bool all_spectrum, float freq_central, float samp_rate, int nintems, float signal_bw, float noise_bw)
    {
      return gnuradio::get_initial_sptr
        (new snr_impl(auto_carrier, carrier, all_spectrum, freq_central, samp_rate, nintems, signal_bw, noise_bw));
    }

    /*
     * The private constructor
     */
    snr_impl::snr_impl(bool auto_carrier, bool carrier, bool all_spectrum, float freq_central, float samp_rate, int nintems, float signal_bw, float noise_bw)
        : gr::sync_block("snr",
                         gr::io_signature::make(1, 1, sizeof(float) * nintems),
                         gr::io_signature::make(1, 1, sizeof(float))),
          d_nintems(nintems), d_auto_carrier(auto_carrier),
          d_samp_rate(samp_rate), d_carrier(carrier),
          d_all_spectrum(all_spectrum),
          d_freq_central_index((freq_central / samp_rate * nintems) + (nintems / 2)),
          signal_item_offset((signal_bw / samp_rate) * (nintems / 4)),
          noise_item_offset((noise_bw / samp_rate) * (nintems / 4))
    {

      d_nintems_half = nintems / 2;
      
      signal_bw_items = signal_item_offset * 2;

      if (d_carrier == true) {
        signal_item_offset = 3; 
        signal_bw_items = 7;
      }

      noise_bw_items = (noise_item_offset - signal_item_offset) * 2;

      if (d_all_spectrum == true)
      {
        noise_item_offset = 0;
        noise_bw_items = d_nintems - signal_bw_items;  
        if(noise_bw_items < 0)
          noise_bw_items = 0;
      }
      check_bands();
      create_buffers();
    }

    snr_impl::~snr_impl()
    {}

    int
    snr_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];
      int index_i = 0;
      float noise = 0;


      for(int i = 0; i < noutput_items; i++) {

        // Perform shift operation
        memcpy(fft_buffer, &in[index_i], sizeof(float) * d_nintems);

        if (d_auto_carrier == true)
        {
          volk_32f_index_max_32u(signal_max_index, fft_buffer, d_nintems);
          d_freq_central_index = *signal_max_index;
        }

        check_bands();

        memcpy(&signal_band[0], &fft_buffer[(d_freq_central_index - signal_item_offset)], sizeof(float) * signal_bw_items);

        

        if (d_all_spectrum == true)
        {
          memcpy(&noise_band[0], &fft_buffer[0], sizeof(float) * (d_freq_central_index - signal_item_offset));
          memcpy(&noise_band[(d_freq_central_index - signal_item_offset)], &fft_buffer[d_freq_central_index + signal_item_offset + 1], sizeof(float) * (d_nintems - (d_freq_central_index + signal_item_offset)));
        }
        
        else
        {
          memcpy(&noise_band[0], &fft_buffer[d_freq_central_index - noise_item_offset], sizeof(float) * (noise_item_offset - signal_item_offset));
          memcpy(&noise_band[(noise_item_offset - signal_item_offset)], &fft_buffer[d_freq_central_index + signal_item_offset + 1], sizeof(float) * (noise_item_offset - signal_item_offset));
        }
        
        volk_32f_accumulator_s32f(noise_acc, noise_band, noise_bw_items);

        volk_32f_accumulator_s32f(signal_acc, signal_band, signal_bw_items);

        noise = *noise_acc;

        if ((d_freq_central_index - signal_item_offset) > d_nintems_half || (d_freq_central_index + signal_item_offset) < d_nintems_half )//to do not evaluate DC component)
            noise -= fft_buffer [d_nintems_half];
            
        out[i] = 10*log10(*signal_acc / noise); 

        index_i = index_i + d_nintems;
      }

      return noutput_items;
    }

    void snr_impl::check_bands()
    {
      if(noise_bw_items == 0 ) {
        throw std::out_of_range ("SNR: The set bandwith of the noise is too small.");
      }

      if((d_freq_central_index + noise_item_offset) >  d_nintems || (d_freq_central_index - noise_item_offset) < 0 ) {
        throw std::out_of_range ("SNR: The set bandwith of the noise exceed the maximum bandwidth given by sampling rate.");
      }
      if((d_freq_central_index + signal_item_offset) >  d_nintems || (d_freq_central_index - signal_item_offset) < 0 ) {
        throw std::out_of_range ("SNR: The set bandwith of the signal exceed the maximum bandwidth given by sampling rate.");
      }
    }


    void snr_impl::create_buffers()
    {
      
      signal_band = (float *)volk_malloc(signal_bw_items * sizeof(float), volk_get_alignment());
      memset(signal_band, 0, signal_bw_items * sizeof(float));

      noise_band = (float *)volk_malloc(noise_bw_items * sizeof(float), volk_get_alignment());
      memset(noise_band, 0, noise_bw_items * sizeof(float));

      temp_buffer = (float *)volk_malloc(sizeof(float) * (d_nintems_half + 1), volk_get_alignment());

      fft_buffer = (float *)volk_malloc(d_nintems * sizeof(float), volk_get_alignment());
      memset(fft_buffer, 0, d_nintems * sizeof(float));

      signal_max_index = (uint32_t *)volk_malloc(sizeof(uint32_t), volk_get_alignment());

      signal_acc = (float *)volk_malloc(sizeof(float), volk_get_alignment());

      noise_acc = (float *)volk_malloc(sizeof(float), volk_get_alignment());
      }

  } /* namespace flaress */
} /* namespace gr */
