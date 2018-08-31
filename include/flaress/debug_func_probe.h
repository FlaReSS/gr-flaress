/* -*- c++ -*- */
/*
 * Copyright 2004,2008,2009,2013,2018 Free Software Foundation, Inc.
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

#ifndef INCLUDED_FLARESS_DEBUG_FUNC_PROBE_H
#define INCLUDED_FLARESS_DEBUG_FUNC_PROBE_H

#include <flaress/api.h>
#include <gnuradio/sync_block.h>
#include <stddef.h>			// size_t

namespace gr {
  namespace flaress {

    /*!
     * \brief debug for function probe
     * \ingroup flaress
     *
     */
    class FLARESS_API debug_func_probe : virtual public gr::sync_block
    {
     public:
      // gr::flaress::debug_func_probe::sptr
      typedef boost::shared_ptr<debug_func_probe> sptr;

      /*!
       * \brief Make a new instance of the vector that contains the absolute nitems read when the debug_nitems() is called,
       * and return a shared pointer to it.
       * \param sizeof_stream_item sizeof_item * length of vector items
       */
      static sptr make(size_t sizeof_stream_item);

      //! Clear the data container.
      virtual void reset() = 0;
      virtual void debug_nitems() = 0;
      virtual std::vector<long int> data() const = 0;
    };

  } // namespace flaress
} // namespace gr

#endif /* INCLUDED_FLARESS_DEBUG_FUNC_PROBE_H */
