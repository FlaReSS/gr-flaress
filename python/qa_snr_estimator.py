#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks, analog
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio import filter
import flaress
import runner, math
import numpy as np

class qa_snr (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """test_001_t: sine wave"""
        tb = self.tb

        samp_rate = 32000
        items = samp_rate * 4 # 4 seconds of simulation
        bw = 100
        dst_src = blocks.vector_sink_c()
        dst_noise = blocks.vector_sink_c()
        dst_noise_bw = blocks.vector_sink_c()
        dst_input = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_f()
        head1 = blocks.head(gr.sizeof_gr_complex, items)
        head2 = blocks.head(gr.sizeof_gr_complex, items)
        
        src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 2000, 1, 0)
        noise = analog.noise_source_c(analog.GR_GAUSSIAN, 0.5, 0)
        
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        throttle2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        
        bpf = filter.fir_filter_ccc(1, firdes.complex_band_pass(
	1, samp_rate, 1000, 3000, 1, firdes.WIN_HAMMING, 6.76))
        
        snr = flaress.snr_estimator_cf(auto_carrier = True, carrier = True, all_spectrum = False, freq_central = 10, samp_rate = samp_rate, nintems = 1024, signal_bw = 0, noise_bw = 2000, avg_alpha = 1.0, average = False, win = window.blackmanharris)
        
        adder = blocks.add_vcc(1)


        tb.connect(src, (adder, 1))
        tb.connect(src, dst_src)
        tb.connect(noise, (adder, 0))
        tb.connect(noise, bpf)
        tb.connect(bpf, dst_noise)
        tb.connect(adder, head1)
        tb.connect(head1, snr)
        tb.connect(snr, dst_out)
        
        
        # tb.connect(noise, throttle2)
        # tb.connect(throttle2, head2)
        # tb.connect(head2, lpf)
        # tb.connect(lpf, dst_noise_bw)
        
        # tb.connect(head, fft)
        
        # tb.connect(fft, snr)
        # tb.connect(snr, dst_out)
        tb.run()
    
        data_src = dst_src.data()
        data_noise = dst_noise.data()
        # data_input = dst_input.data()
        data_out = dst_out.data()


        print "SNR Fs:",10*math.log10(np.var(data_src) / np.var(data_noise))
        print "SNR ESTIMATOR:", np.mean(data_out)


if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_snr)
    runner = runner.HTMLTestRunner(output='Results',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()