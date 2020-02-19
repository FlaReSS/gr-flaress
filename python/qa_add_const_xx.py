#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import flaress_swig as flaress
import runner, pmt, math

class qa_add_const_xx (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_int64_2 (self):
        """test_001_int64_2: add const int64 version with 2 inputs"""

        src_data1 = [int(x) for x in range(16)]
        expected_result_temp = []

        const = 10
        for i in range(0, len(src_data1)): 
            expected_result_temp.append(const + src_data1[i])
        expected_result = tuple(expected_result_temp)

        src1 = flaress.vector_source_int64(src_data1)
        dst = flaress.vector_sink_int64()

        op = flaress.add_const_int64(const, 1)

        self.tb.connect(src1, (op, 0))
        self.tb.connect(op, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)

    def test_002_double_2 (self):
        """test_002_double_2: add const double version with 2 inputs"""

        src_data1 = [float(x) for x in range(16)]
        expected_result_temp = []

        const = 10
        for i in range(0, len(src_data1)): 
            expected_result_temp.append(const + src_data1[i])
        expected_result = tuple(expected_result_temp)

        src1 = flaress.vector_source_double(src_data1)
        dst = flaress.vector_sink_double()

        op = flaress.add_const_double(const, 1)

        self.tb.connect(src1, (op, 0))
        self.tb.connect(op, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)
      
if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_add_const_xx)
    runner = runner.HTMLTestRunner(output='Results', template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()
