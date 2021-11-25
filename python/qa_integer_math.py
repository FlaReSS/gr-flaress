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

class qa_integer_math (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """test_001_t: int input"""
        src_data = np.arange(-10, 10, 1)
        expected_result = (-8, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 7, 7)

        src = blocks.vector_source_i(src_data)
        dst = blocks.vector_sink_i()
        integer_point_math_conv = flaress.integer_math_ii(1, 4)

        self.tb.connect(src, integer_point_math_conv, dst)
        self.tb.run()

        result_data = dst.data()

        # print result_data
        self.assertEqual(expected_result, result_data)

    def test_002_t (self):
        """test_002_t: long input"""
        src_data = np.arange(-10, 10, 1)
        expected_result = (-8, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 7, 7)

        src = flaress.vector_source_int64(src_data)
        dst = flaress.vector_sink_int64()
        integer_point_math_conv = flaress.integer_math_ll(1, 4)

        self.tb.connect(src, integer_point_math_conv, dst)
        self.tb.run()

        result_data = dst.data()

        # print result_data
        self.assertEqual(expected_result, result_data)


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_integer_math)
    runner = runner.HTMLTestRunner(output='../TestResults',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()