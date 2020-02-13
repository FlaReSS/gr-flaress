#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks, analog
import runner, threading, time, pmt, math
import flaress_swig as flaress

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

class qa_selector (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_c (self):
        """test_001_c: mux complex version with 2 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 2, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_gr_complex*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        dst_in0 = blocks.vector_sink_c()
        dst_in1 = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_c()
        head_out = blocks.head(gr.sizeof_gr_complex, N)
        sig_source0 = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)

        # Connections
        tb.connect(sig_source0,throttle0)
        tb.connect(sig_source1,throttle1)
        tb.connect(throttle0, dst_in0)
        tb.connect(throttle1, dst_in1)
        tb.connect(throttle0, (flaress_selector, 0))
        tb.connect(throttle1, (flaress_selector, 1))
        tb.connect(flaress_selector, head_out, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()

        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                    N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_001_f (self):
        """test_001_f: mux float version with 2 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_float*1, 0, 2, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_float*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(gr.sizeof_float*1, samp_rate, True)
        throttle1 = blocks.throttle(gr.sizeof_float*1, samp_rate, True)
        dst_in0 = blocks.vector_sink_f()
        dst_in1 = blocks.vector_sink_f()
        dst_out = blocks.vector_sink_f()
        head0 = blocks.head(gr.sizeof_float, N)
        head1 = blocks.head(gr.sizeof_float, N)
        sig_source0 = analog.sig_source_f(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_f(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)

        # Connections
        tb.connect(sig_source0,throttle0)
        tb.connect(sig_source1,throttle1)
        tb.connect(throttle0, head0)
        tb.connect(throttle1, head1)
        tb.connect(head0, dst_in0)
        tb.connect(head1, dst_in1)
        tb.connect(head0, (flaress_selector, 0))
        tb.connect(head1, (flaress_selector, 1))
        tb.connect(flaress_selector, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()
        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                    N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_001_d (self):
        """test_001_d: mux double version with 2 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_double*1, 0, 2, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_double*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(gr.sizeof_double*1, samp_rate, True)
        throttle1 = blocks.throttle(gr.sizeof_double*1, samp_rate, True)
        dst_in0 = flaress.vector_sink_double()
        dst_in1 = flaress.vector_sink_double()
        dst_out = flaress.vector_sink_double()
        head0 = blocks.head(gr.sizeof_double, N)
        head1 = blocks.head(gr.sizeof_double, N)
        sig_source0 = analog.sig_source_f(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_f(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)
        conv_in0 = flaress.float_to_double()
        conv_in1 = flaress.float_to_double()

        # throttle0.set_max_noutput_items (samp_rate)
        # throttle1.set_max_noutput_items (samp_rate)
        # throttle0.set_min_noutput_items (samp_rate)
        # throttle1.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source0, conv_in0, throttle0)
        tb.connect(sig_source1, conv_in1,throttle1)
        tb.connect(throttle0, head0)
        tb.connect(throttle1, head1)
        tb.connect(head0, dst_in0)
        tb.connect(head1, dst_in1)
        tb.connect(head0, (flaress_selector, 0))
        tb.connect(head1, (flaress_selector, 1))
        tb.connect(flaress_selector, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()
        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_001_i (self):
        """test_001_i: mux int version with 2 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_int*1, 0, 2, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_int*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(gr.sizeof_int*1, samp_rate, True)
        throttle1 = blocks.throttle(gr.sizeof_int*1, samp_rate, True)
        dst_in0 = blocks.vector_sink_i()
        dst_in1 = blocks.vector_sink_i()
        dst_out = blocks.vector_sink_i()
        head0 = blocks.head(gr.sizeof_int, N)
        head1 = blocks.head(gr.sizeof_int, N)
        sig_source0 = analog.sig_source_i(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_i(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)

        # throttle0.set_max_noutput_items (samp_rate)
        # throttle1.set_max_noutput_items (samp_rate)
        # throttle0.set_min_noutput_items (samp_rate)
        # throttle1.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source0,throttle0)
        tb.connect(sig_source1,throttle1)
        tb.connect(throttle0, head0)
        tb.connect(throttle1, head1)
        tb.connect(head0, dst_in0)
        tb.connect(head1, dst_in1)
        tb.connect(head0, (flaress_selector, 0))
        tb.connect(head1, (flaress_selector, 1))
        tb.connect(flaress_selector, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()
        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                    N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_001_l (self):
        """test_001_l: mux int64 version with 2 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(flaress.sizeof_long*1, 0, 2, 1)
        debug_switch = flaress.debug_func_probe(flaress.sizeof_long*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(flaress.sizeof_long*1, samp_rate, True)
        throttle1 = blocks.throttle(flaress.sizeof_long*1, samp_rate, True)
        dst_in0 = flaress.vector_sink_int64()
        dst_in1 = flaress.vector_sink_int64()
        dst_out = flaress.vector_sink_int64()
        head0 = blocks.head(flaress.sizeof_long, N)
        head1 = blocks.head(flaress.sizeof_long, N)
        sig_source0 = analog.sig_source_i(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_i(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)
        conv_in0 = flaress.int_to_int64()
        conv_in1 = flaress.int_to_int64()

        # throttle0.set_max_noutput_items (samp_rate)
        # throttle1.set_max_noutput_items (samp_rate)
        # throttle0.set_min_noutput_items (samp_rate)
        # throttle1.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source0, conv_in0, throttle0)
        tb.connect(sig_source1, conv_in1,throttle1)
        tb.connect(throttle0, head0)
        tb.connect(throttle1, head1)
        tb.connect(head0, dst_in0)
        tb.connect(head1, dst_in1)
        tb.connect(head0, (flaress_selector, 0))
        tb.connect(head1, (flaress_selector, 1))
        tb.connect(flaress_selector, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()
        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                    N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_002_c (self):
        """test_002_c: mux version with 3 inputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 4

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 3, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_gr_complex*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
                time.sleep(1)
            except AttributeError:
                pass
            try:
                flaress_selector.set_select(2)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        throttle2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        dst_in0 = flaress.vector_sink_double()
        dst_in1 = flaress.vector_sink_double()
        dst_in2 = flaress.vector_sink_double()
        dst_out = flaress.vector_sink_double()
        head = blocks.head(gr.sizeof_gr_complex, N)
        sig_source0 = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)
        sig_source1 = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 11)
        sig_source2 = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , -10, -1)

        # Connections
        tb.connect(sig_source0, throttle0)
        tb.connect(sig_source1, throttle1)
        tb.connect(sig_source2, throttle2)
        tb.connect(throttle0, dst_in0)
        tb.connect(throttle1, dst_in1)
        tb.connect(throttle2, dst_in2)
        tb.connect(throttle0, (flaress_selector, 0))
        tb.connect(throttle1, (flaress_selector, 1))
        tb.connect(throttle2, (flaress_selector, 2))
        tb.connect(flaress_selector, head, dst_out)
        tb.connect(flaress_selector, debug_switch)

        _probe_func_thread.start()
        tb.run()

        data_in_0 = dst_in0.data()
        data_in_1 = dst_in1.data()
        data_in_2 = dst_in2.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = 0
        N_sel1 = 0
        N_sel2 = 0
        N_out = len(data_out)

        for i in range(N):
            if (data_out[i] == data_in_0[i]):
                N_sel0 += 1
            elif (data_out[i] == data_in_1[(i)]):
                N_sel1 += 1
            elif (data_out[i] == data_in_2[(i)]):
                N_sel2 += 1
            else:
                lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertGreater(N_sel2, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1 + N_sel2), N)

        print ("- Items outputted from in0: ", N_sel0)
        print ("- Items outputted from in1: ", N_sel1)
        print ("- Items outputted from in2: ", N_sel2)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 2)
        self.assertEqual(self.debug_select, 2)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- First Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))
        print ("- Second Set function received at the moment (of the simulation): %.2f s;" % (switch[1] * (1.0 / samp_rate)))

    def test_003_c (self):
        """test_003_c: demux version with 2 outputs"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 3

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 1, 2)
        debug_switch = flaress.debug_func_probe(gr.sizeof_gr_complex*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        dst_in = blocks.vector_sink_c()
        dst_out0 = blocks.vector_sink_c()
        dst_out1 = blocks.vector_sink_c()
        head = blocks.head(gr.sizeof_gr_complex, N)
        sig_source = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, float(samp_rate / N) , 10, 0)

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source,throttle)
        tb.connect(throttle, head)
        tb.connect(head, dst_in)
        tb.connect(head, flaress_selector)
        tb.connect(head, debug_switch)
        tb.connect((flaress_selector, 0), dst_out0)
        tb.connect((flaress_selector, 1), dst_out1)

        _probe_func_thread.start()
        tb.run()

        data_in = dst_in.data()
        data_out_0 = dst_out0.data()
        data_out_1 = dst_out1.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = len(data_out_0)
        N_sel1 = len(data_out_1)
        for i in range(N):
            if ( i < N_sel0):
                if (data_in[i] != data_out_0[i]):
                    lost_items += 1
            else:
                if (data_in[i] != data_out_1[i - N_sel0]):
                    lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1), N)

        print ("- Items outputted on out0: ",N_sel0)
        print ("- Items outputted on out1: ", N_sel1)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 1)
        self.assertEqual(self.debug_select, 1)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))

    def test_004_c (self):
        """test_004_c: demux version with 3 outpus"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 4

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 1, 3)
        debug_switch = flaress.debug_func_probe(gr.sizeof_gr_complex*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
                time.sleep(1)
            except AttributeError:
                pass
            try:
                flaress_selector.set_select(2)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        dst_in = blocks.vector_sink_c()
        dst_out0 = blocks.vector_sink_c()
        dst_out1 = blocks.vector_sink_c()
        dst_out2 = blocks.vector_sink_c()
        head = blocks.head(gr.sizeof_gr_complex, N)
        sig_source = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, float(samp_rate / N) , 10, 0)

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source,throttle)
        tb.connect(throttle, head)
        tb.connect(head, dst_in)
        tb.connect(head, flaress_selector)
        tb.connect(head, debug_switch)
        tb.connect((flaress_selector, 0), dst_out0)
        tb.connect((flaress_selector, 1), dst_out1)
        tb.connect((flaress_selector, 2), dst_out2)

        _probe_func_thread.start()
        tb.run()

        data_in = dst_in.data()
        data_out_0 = dst_out0.data()
        data_out_1 = dst_out1.data()
        data_out_2 = dst_out2.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel0 = len(data_out_0)
        N_sel1 = len(data_out_1)
        N_sel2 = len(data_out_2)
        for i in range(N):
            if ( i < N_sel0):
                if (data_in[i] != data_out_0[i]):
                    lost_items += 1
            elif ( i < (N_sel0 + N_sel1)):
                if (data_in[i] != data_out_1[i - N_sel0]):
                    lost_items += 1
            else:
                if (data_in[i] != data_out_2[i - (N_sel0 + N_sel1)]):
                    lost_items += 1

        self.assertGreater(N_sel0, 0)
        self.assertGreater(N_sel1, 0)
        self.assertGreater(N_sel2, 0)
        self.assertEqual(lost_items, 0)
        self.assertEqual((N_sel0 + N_sel1 + N_sel2), N)


        print ("- Items outputted on out0: ",N_sel0)
        print ("- Items outputted on out1: ", N_sel1)
        print ("- Items outputted on out2: ", N_sel2)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 2)
        self.assertEqual(self.debug_select, 2)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- First Set function received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))
        print ("- Second et function received at the moment (of the simulation): %.2f s;" % (switch[1] * (1.0 / samp_rate)))

    def test_005_c (self):
        """test_005_c: mux complex version in switcher mode"""

        tb = self.tb

        # Variables
        samp_rate = 4096
        N = samp_rate * 4

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 1, 1)
        debug_switch = flaress.debug_func_probe(gr.sizeof_gr_complex*1)

        def _probe_func_probe():
            time.sleep(1)
            try:
                flaress_selector.set_select(-1)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
                time.sleep(1)
            except AttributeError:
                pass
            try:
                flaress_selector.set_select(0)
                debug_switch.debug_nitems()
                self.debug_select = flaress_selector.get_select()
            except AttributeError:
                pass

        _probe_func_thread = threading.Thread(target=_probe_func_probe)
        _probe_func_thread.daemon = True

        throttle = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True)
        dst_in = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_c()
        head = blocks.head(gr.sizeof_gr_complex, N)
        sig_source = analog.sig_source_c(samp_rate,analog.GR_SAW_WAVE, 0.125 , 10, 0)

        # throttle.set_max_noutput_items (samp_rate)
        # throttle.set_min_noutput_items (samp_rate)

        # Connections
        tb.connect(sig_source,throttle)
        tb.connect(throttle, head)
        tb.connect(head, dst_in)
        tb.connect(head, debug_switch)
        tb.connect(head, flaress_selector)
        tb.connect(flaress_selector, dst_out)

        _probe_func_thread.start()
        tb.run()

        data_in = dst_in.data()
        data_out = dst_out.data()
        switch = debug_switch.data()

        # Checking
        lost_items = 0
        N_sel = 0
        N_out = len(data_out)

        for i in range(N):
            try:
                if (data_out.index(data_in[i]) >= 0):
                    N_sel += 1
            except ValueError:
                lost_items += 1

        self.assertGreater(N_sel, 0)
        self.assertGreater(lost_items, 0)
        self.assertEqual(N_sel + lost_items, N)

        print ("- Items outputted from in: ", N)
        print ("- Items lost: ", lost_items)

        #check the switch
        self.assertEqual(len(switch), 2)
        self.assertEqual(self.debug_select, 0)
        print ("- Final order of the selector: %d;" %self.debug_select)
        print ("- First Set function (Turn OFF) received at the moment (of the simulation): %.2f s;" % (switch[0] * (1.0 / samp_rate)))
        print ("- Second Set function (Turn ON) received at the moment (of the simulation): %.2f s;" % (switch[1] * (1.0 / samp_rate)))

    def test_006_c (self):
        """test_006_c: mux complex version with tagged streams"""

        tb = self.tb

        # Variables
        samp_rate = 1024
        N = samp_rate * 4

        # Data
        src_data = [complex(x) for x in range(N)]
        expected_result = src_data[:]

        src_tags0 = tuple([ make_tag('key0', 'val0', 0, 'src0'),
                            make_tag('key0', 'val0', (N / 4), 'src0'),
                            make_tag('key0', 'val0', (N / 3), 'src0'),
                            make_tag('key0', 'val0', (N / 2), 'src0')])

        src_tags1 = tuple([ make_tag('key1', 'val1', 0, 'src1'),
                            make_tag('key1', 'val1', (N / 4), 'src1'),
                            make_tag('key1', 'val1', (N / 3), 'src1'),
                            make_tag('key1', 'val1', (N / 2), 'src1')])

        expected_tags =src_tags0[:]

        # Blocks
        flaress_selector = flaress.selector(gr.sizeof_gr_complex*1, 0, 2, 1)
        dst_out = blocks.vector_sink_c()
        head = blocks.head(gr.sizeof_gr_complex, N)
        sig_source0 = blocks.vector_source_c(src_data, repeat=False, tags=src_tags0)
        sig_source1 = blocks.vector_source_c(src_data, repeat=False, tags=src_tags1)


        # Connections
        tb.connect(sig_source0, (flaress_selector, 0))
        tb.connect(sig_source1, (flaress_selector, 1))
        tb.connect(flaress_selector, dst_out)

        self.tb.run()

        result_data = dst_out.data()
        result_tags = dst_out.tags()

        self.assertFloatTuplesAlmostEqual(expected_result, result_data)
        self.assertEqual(len(result_tags), 4)
        self.assertTrue(compare_tags(expected_tags[0], result_tags[0]))
        self.assertTrue(compare_tags(expected_tags[1], result_tags[1]))
        self.assertTrue(compare_tags(expected_tags[2], result_tags[2]))
        self.assertTrue(compare_tags(expected_tags[3], result_tags[3]))

        print ("- Tag received properly")

if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_selector)
    runner = runner.HTMLTestRunner(output='Results', template='DEFAULT_TEMPLATE_2')
    runner.run(suite)
    #gr_unittest.TestProgram()
