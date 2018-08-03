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

#ifndef INCLUDED_FLARESS_SELECTOR_IMPL_H
#define INCLUDED_FLARESS_SELECTOR_IMPL_H

#include <flaress/selector.h>

namespace gr {
  namespace flaress {

    class selector_impl : public selector
    {
     private:
      size_t d_sizeof_stream_item;
      int d_select;
      int d_n_inputs;
      int d_n_outputs;
      int out_sel, in_sel;

     public:
      selector_impl(size_t sizeof_stream_item, int select, int n_inputs, int n_outputs);
      ~selector_impl();

      // Where all the action really happens
      int general_work (int noutput_items,
                         gr_vector_int &ninput_items,
                         gr_vector_const_void_star &input_items,
                         gr_vector_void_star &output_items);

      void sel_evaluation();
      int get_select() const;
      void set_select(int select);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_SELECTOR_IMPL_H */
