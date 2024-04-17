#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import flaress_swig as flaress
import runner, pmt, math

def make_tag(key, value, offset, srcid=None):
    tag = gr.tag_t()
    tag.key = pmt.string_to_symbol(key)
    tag.value = pmt.to_pmt(value)
    tag.offset = offset
    if srcid is not None:
        tag.srcid = pmt.to_pmt(srcid)
    return tag

def compare_tags(a, b):
    return a.offset == b.offset and pmt.equal(a.key, b.key) and \
           pmt.equal(a.value, b.value) and pmt.equal(a.srcid, b.srcid)

class qa_float_to_double (gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001(self):
        """test_001: that sink has data set in source for the simplest case"""
        
        src_data = [float(x) for x in range(16)]
        expected_result = tuple(src_data)

        src = blocks.vector_source_f(src_data)
        dst = flaress.vector_sink_int64()
        conv = flaress.float_to_int64()

        self.tb.connect(src, conv, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)

    def test_002(self):
        """test_002: vectors (the gnuradio vector I/O type)"""
        
        src_data = [float(x) for x in range(16)]
        expected_result = tuple(src_data)

        src = blocks.vector_source_f(src_data, False, 2)
        dst = flaress.vector_sink_int64(2)
        conv = flaress.float_to_int64(2)

        self.tb.connect(src, conv, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)

    def test_003(self):
        """test_003: sending and receiving tagged streams"""
        
        src_data = [float(x) for x in range(16)]
        expected_result = tuple(src_data)
        src_tags = tuple([make_tag('key', 'val', 0, 'src')])
        expected_tags = src_tags[:]

        src = blocks.vector_source_f(src_data, repeat=False, tags=src_tags)
        dst = flaress.vector_sink_int64()
        conv = flaress.float_to_int64()

        self.tb.connect(src, conv, dst)
        self.tb.run()
        result_data = dst.data()
        result_tags = dst.tags()
        self.assertEqual(expected_result, result_data)
        self.assertEqual(len(result_tags), 1)
        self.assertTrue(compare_tags(expected_tags[0], result_tags[0]))

    def test_004(self):
        """test_004: set_data"""

        src_data = [float(x) for x in range(16)]
        expected_result = tuple(src_data)

        src = blocks.vector_source_f((3,1,4))
        dst = flaress.vector_sink_int64()
        src.set_data(src_data)
        conv = flaress.float_to_int64()

        self.tb.connect(src, conv, dst)
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)

    def test_005(self):
        """test_005: set_repeat"""
       
        src_data = [float(x) for x in range(16)]
        expected_result = tuple(src_data)

        src = blocks.vector_source_f(src_data, True)
        dst = flaress.vector_sink_int64()
        src.set_repeat(False)
        conv = flaress.float_to_int64()

        self.tb.connect(src, conv, dst)
        # will timeout if set_repeat does not work
        self.tb.run()
        result_data = dst.data()
        self.assertEqual(expected_result, result_data)

if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_float_to_double)
    runner = runner.HTMLTestRunner(output='../TestResults', template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()