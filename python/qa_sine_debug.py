#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
import flaress_swig as flaress
from sine_debug import sine_debug
import runner, time, math
import numpy as np
from gnuradio import blocks, analog

class qa_sine_debug (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001(self):
        """test_001: with sine wave"""

        tb = self.tb

        # Variables
        samp_rate = 4096 * 32
        items = samp_rate / 2
        step_phase = 2.0
        frequency = step_phase * samp_rate / (2 * math.pi)

        # Blocks
        sine_debug_0 = sine_debug()
        dst_out = blocks.vector_sink_f()
        head = blocks.head(gr.sizeof_gr_complex, items)
        sig_source = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, frequency, 1, 0)


        # Connections
        tb.connect(sig_source, head)
        tb.connect(head, sine_debug_0)
        tb.connect(sine_debug_0, dst_out)

        self.tb.run()

        result_data = dst_out.data()

        self.assertAlmostEqual(np.mean(result_data), step_phase, 4)
        self.assertAlmostEqual(np.var(result_data), 0, 3)
        print(np.mean(result_data), np.var(result_data))

    def test_002(self):
        """test_002: with cossine wave"""

        tb = self.tb

        # Variables
        samp_rate = 4096 * 32
        items = samp_rate / 2
        step_phase = 3.0
        frequency = step_phase * samp_rate / (2 * math.pi)

        # Blocks
        sine_debug_0 = sine_debug()
        dst_out = blocks.vector_sink_f()
        head = blocks.head(gr.sizeof_gr_complex, items)
        sig_source = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, frequency, 1, 0)


        # Connections
        tb.connect(sig_source, head)
        tb.connect(head, sine_debug_0)
        tb.connect(sine_debug_0, dst_out)

        self.tb.run()

        result_data = dst_out.data()

        self.assertAlmostEqual(np.mean(result_data), step_phase, 4)
        self.assertAlmostEqual(np.var(result_data), 0, 3)
        print(np.mean(result_data), np.var(result_data))


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_sine_debug)
    runner = runner.HTMLTestRunner(output='../TestResults',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()
