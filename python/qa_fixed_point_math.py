#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
import flaress_swig as flaress
import runner, time
import numpy as np
from gnuradio import blocks, analog

class qa_fixed_point_math_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """test_001_t: fractional"""
        src_data = np.arange(-2, 2, 0.01)
        expected_result = (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.9375, -0.9375, -0.9375, -0.9375, -0.9375, -0.9375, -0.875, -0.875, -0.875, -0.875, -0.875, -0.875, -0.8125, -0.8125, -0.8125, -0.8125, -0.8125, -0.8125, -0.75, -0.75, -0.75, -0.75, -0.75, -0.75, -0.75, -0.6875, -0.6875, -0.6875, -0.6875, -0.6875, -0.6875, -0.625, -0.625, -0.625, -0.625, -0.625, -0.625, -0.5625, -0.5625, -0.5625, -0.5625, -0.5625, -0.5625, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.4375, -0.4375, -0.4375, -0.4375, -0.4375, -0.4375, -0.375, -0.375, -0.375, -0.375, -0.375, -0.375, -0.3125, -0.3125, -0.3125, -0.3125, -0.3125, -0.3125, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.25, -0.1875, -0.1875, -0.1875, -0.1875, -0.1875, -0.1875, -0.125, -0.125, -0.125, -0.125, -0.125, -0.125, -0.0625, -0.0625, -0.0625, -0.0625, -0.0625, -0.0625, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.0625, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.1875, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.3125, 0.3125, 0.3125, 0.3125, 0.3125, 0.3125, 0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.4375, 0.4375, 0.4375, 0.4375, 0.4375, 0.4375, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5625, 0.5625, 0.5625, 0.5625, 0.5625, 0.5625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.625, 0.6875, 0.6875, 0.6875, 0.6875, 0.6875, 0.6875, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.8125, 0.8125, 0.8125, 0.8125, 0.8125, 0.8125, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375,0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375, 0.9375)

        src = blocks.vector_source_f(src_data)
        dst = blocks.vector_sink_f()
        fixed_point_math_conv = flaress.fixed_point_math_ff(1, 1, 4)

        self.tb.connect(src, fixed_point_math_conv, dst)
        self.tb.run()

        result_data = dst.data()

        # print result_data
        self.assertEqual(expected_result, result_data)


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_fixed_point_math_cc)
    runner = runner.HTMLTestRunner(output='Results',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()