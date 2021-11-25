#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import runner
import flaress_swig as flaress

class qa_null_source_sink (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001(self):
        """test_001: with Float"""
        src = flaress.null_source(gr.sizeof_float)
        head = blocks.head(gr.sizeof_float, 100)
        dst = flaress.null_sink(gr.sizeof_float)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_002(self):
        """test_002: with Int"""
        src = flaress.null_source(gr.sizeof_int)
        head = blocks.head(gr.sizeof_int, 100)
        dst = flaress.null_sink(gr.sizeof_int)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_003(self):
        """test_003: with Short"""
        src = flaress.null_source(gr.sizeof_short)
        head = blocks.head(gr.sizeof_short, 100)
        dst = flaress.null_sink(gr.sizeof_short)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_004(self):
        """test_004: with Byte"""
        src = flaress.null_source(gr.sizeof_char)
        head = blocks.head(gr.sizeof_char, 100)
        dst = flaress.null_sink(gr.sizeof_char)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_005(self):
        """test_005: with Int64"""
        src = flaress.null_source(flaress.sizeof_long)
        head = blocks.head(flaress.sizeof_long, 100)
        dst = flaress.null_sink(flaress.sizeof_long)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_006(self):
        """test_006: with Float64 (Double)"""
        src = flaress.null_source(gr.sizeof_double)
        head = blocks.head(gr.sizeof_double, 100)
        dst = flaress.null_sink(gr.sizeof_double)

        self.tb.connect(src, head, dst)
        self.tb.run()

    def test_007(self):
        """test_007: with Complex"""
        src = flaress.null_source(gr.sizeof_gr_complex)
        head = blocks.head(gr.sizeof_gr_complex, 100)
        dst = flaress.null_sink(gr.sizeof_gr_complex)

        self.tb.connect(src, head, dst)
        self.tb.run()


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_null_source_sink)
    runner = runner.HTMLTestRunner(output='../TestResults', template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()