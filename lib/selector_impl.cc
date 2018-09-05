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
#include "selector_impl.h"

namespace gr {
  namespace flaress {

    selector::sptr
    selector::make(size_t sizeof_stream_item, int select, int n_inputs, int n_outputs)
    {
      return gnuradio::get_initial_sptr
        (new selector_impl(sizeof_stream_item, select, n_inputs, n_outputs));
    }

    selector_impl::selector_impl(size_t sizeof_stream_item, int select, int n_inputs, int n_outputs)
      : gr::block("selector",
              gr::io_signature::make(0, n_inputs, sizeof_stream_item),
              gr::io_signature::make(0, n_outputs, sizeof_stream_item)),
              d_select(select), d_n_inputs(n_inputs), d_n_outputs(n_outputs),
              d_sizeof_stream_item(sizeof_stream_item)
    {}

    selector_impl::~selector_impl()
    {}

    void
    selector_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      for(int w = 0; w < d_n_inputs; w++) {
          ninput_items_required[w] = noutput_items;
      }
    }

    int
    selector_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        if (d_select != -1){

        sel_evaluation();
        void *in = (void*) input_items[in_sel];
        void *out = (void *) output_items[out_sel];

        // std::cout << "noutput_items: " << noutput_items << '\n';

        memcpy(out, in, noutput_items * d_sizeof_stream_item);

        for(int w = 0; w < d_n_outputs; w++) {
          if (w != out_sel )
            produce(w, 0);
          else
            produce(w, noutput_items);
        }
        consume_each(noutput_items);
        return WORK_CALLED_PRODUCE;
      }
      else{
        consume_each(noutput_items);
        return 0;
      }
    }

    void selector_impl::sel_evaluation(){
      static int temp = 0;
      if ( d_n_inputs > 1)
      {
        out_sel = 0;
        in_sel = d_select;
      }
      else
      {
        out_sel = d_select;
        in_sel = 0;
      }
    }

    int selector_impl::get_select() const   { return d_select;  }

    void selector_impl::set_select(int select)
    {
      int max, temp;
      temp = select;
      if (d_n_inputs >= d_n_outputs)
        max = d_n_inputs;
      else
        max = d_n_outputs;

      if(select >= max) {
        temp = 0;
        throw std::out_of_range ("pll: invalid selector value, too high.");

      }
      if (select < -1) {
        temp = -1;
        throw std::out_of_range ("pll: invalid selector value, too low.");

      }
      d_select = temp;
    }


  } /* namespace flaress */
} /* namespace gr */
