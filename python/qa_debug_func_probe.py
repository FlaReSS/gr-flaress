#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
import flaress_swig as flaress
import runner, threading, time
from gnuradio import blocks, analog

class qa_debug_func_probe (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """test_001_t: one set function after 0.5 seconds"""

        tb = self.tb

        samp_rate = 4096
        items = samp_rate * 2 # 3 seconds of simulation


        debug = flaress.debug_func_probe(gr.sizeof_float*1)

        def _probe_func_probe():
            time.sleep(0.5)
            try:
                debug.debug_nitems()
            except AttributeError:
                pass
        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        src = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 0, 0, 0)
        throttle = blocks.throttle(gr.sizeof_float*1, samp_rate)
        head = blocks.head(gr.sizeof_float, int (items))
        dst = blocks.null_sink(gr.sizeof_float*1)

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        tb.connect(src, throttle)
        tb.connect(throttle, head)
        tb.connect(head, debug)

        _probe_func_thread.start()
        tb.run()

        data = debug.data()

        self.assertEqual(len(data), 1)
        self.assertLessEqual(data[0], samp_rate*2)

        print ("-Set function received at the moment: %f s." % (data[0] * (1.0 / samp_rate)))

    def test_002_t (self):
        """test_002_t: one set function after 1 second"""

        tb = self.tb

        samp_rate = 4096
        items = samp_rate * 3 # 3 seconds of simulation


        debug = flaress.debug_func_probe(gr.sizeof_float*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                debug.debug_nitems()
            except AttributeError:
                pass
        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        src = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 0, 0, 0)
        throttle = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        head = blocks.head(gr.sizeof_float, int (items))

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        tb.connect(src, throttle)
        tb.connect(throttle, head)
        tb.connect(head, debug)

        _probe_func_thread.start()
        tb.run()

        data = debug.data()

        self.assertEqual(len(data), 1)
        self.assertLessEqual(data[0], samp_rate * 2)
        self.assertGreaterEqual(data[0], samp_rate)

        print ("-Set function received at the moment: %f s." % (data[0] * (1.0 / samp_rate)))

    def test_003_t (self):
        """test_003_t: two set function after 1 second and 2 seconds"""

        tb = self.tb

        samp_rate = 4096    #under 4096 does not work so fast.
        items = samp_rate * 3 # 3 seconds of simulation


        debug = flaress.debug_func_probe(gr.sizeof_float*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                debug.debug_nitems()
            except AttributeError:
                pass
            time.sleep(1)
            try:
                debug.debug_nitems()
            except AttributeError:
                pass
        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        src = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 0, 0, 0)
        throttle = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        head = blocks.head(gr.sizeof_float, int (items))

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        tb.connect(src, throttle)
        tb.connect(throttle, head)
        tb.connect(head, debug)

        _probe_func_thread.start()
        tb.run()

        data = debug.data()

        self.assertEqual(len(data), 2)
        self.assertLessEqual(data[0], samp_rate * 2)
        self.assertGreaterEqual(data[0], samp_rate)
        self.assertLessEqual(data[1], samp_rate * 3)
        self.assertGreaterEqual(data[1], samp_rate * 2)

        print ("-Set function received at the moment: %f s." % (data[0] * (1.0 / samp_rate)))
        print ("-Set function received at the moment: %f s." % (data[1] * (1.0 / samp_rate)))


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_debug_func_probe)
    runner = runner.HTMLTestRunner(output='Results',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()
