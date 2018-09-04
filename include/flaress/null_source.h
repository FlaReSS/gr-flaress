/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013,2017-2018 Free Software Foundation, Inc.
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

#ifndef INCLUDED_FLARESS_NULL_SOURCE_H
#define INCLUDED_FLARESS_NULL_SOURCE_H

#include <flaress/api.h>
#include <gnuradio/sync_block.h>

    namespace gr {
  namespace flaress {

  /*!
     * \brief A source of zeros used mainly for testing.
     * \ingroup misc_blk
     */
  class FLARESS_API null_source : virtual public gr::sync_block
  {
  public:
    // gr::flaress::null_source::sptr
    typedef boost::shared_ptr<null_source> sptr;

    /*!
       * Build a null source block.
       *
       * \param sizeof_stream_item size of the stream items in bytes.
       */
    static sptr make(size_t sizeof_stream_item);
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_NULL_SOURCE_H */

