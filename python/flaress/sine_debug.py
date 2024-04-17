#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

import numpy
from gnuradio import gr
import numpy as np

class sine_debug(gr.sync_block):
    """
    this block essentially evaluates the derivative of phase (Arg) of input signal. This calculus is used to check if the input sine wave has phase jumps, if not, the output will be a costant.
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="sine_debug",
            in_sig=[numpy.complex64],
            out_sig=[numpy.float32])
        self.d_in = 0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        d_phase = 0
        for i in range(len(in0)):
            temp = in0[i] * np.conjugate(self.d_in)
            out0[i] = np.arctan2(temp.imag, temp.real)
            self.d_in = in0[i]
        return len(input_items[0])

