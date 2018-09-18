#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

import numpy, math
from gnuradio import gr


class sine_debug(gr.sync_block):
    """
    docstring for block sine_debug
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="sine_debug",
            in_sig=[numpy.complex64],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        d_phase = 0
        for i in range(len(in0)):
            phase = math.atan2(in0[i].imag, in0[i].real)

            if (i == 0):
                step = abs(phase)

            if (abs(d_phase) + step) <= math.pi:
                if abs(phase - d_phase) - step > 0.1:
                    print "WARNING: jump phase of:",abs(phase - d_phase)
                    step = abs(phase - d_phase)

            d_phase = phase

        return len(input_items[0])

