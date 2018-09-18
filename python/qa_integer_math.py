#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
import flaress_swig as flaress
import runner, time
from gnuradio import blocks, analog

class qa_integer_math_ii (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """"test_001_t: """"
        self.tb.run ()


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_integer_math_ii)
    runner = runner.HTMLTestRunner(output='Results',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()