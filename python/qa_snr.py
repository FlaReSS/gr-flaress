#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks, analog
from gnuradio.fft import logpwrfft
import flaress_swig as flaress
import runner, math
import numpy as np

class qa_snr (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    # def test_000_t (self):
    #     """test_000_t: snr define wave"""
    #     tb = self.tb

            
    #     samp_rate = 4096 * 4
    #     items = samp_rate * 10 # 3 seconds of simulation

    #     snr = 50

    #     dst_src = blocks.vector_sink_c()
    #     dst_noise = blocks.vector_sink_c()
    #     dst_input = blocks.vector_sink_c()
    #     dst_out = blocks.vector_sink_f()
    #     head = blocks.head(gr.sizeof_gr_complex, items)

    #     src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 1000, 1, 0)
    #     noise = analog.noise_source_c(analog.GR_GAUSSIAN, 10^(-snr/40), 0)
    #     snr = flaress.snr(True, samp_rate, 1024, 100, 5000)
    #     adder = blocks.add_vcc(1)
    #     fft = logpwrfft.logpwrfft_c(
    #         sample_rate=samp_rate,
    #         fft_size=1024,
    #         ref_scale=2,
    #         frame_rate=30,
    #         avg_alpha=0.5,
    #         average=False,
    #     )


    #     tb.connect(src, (adder, 1))
    #     tb.connect(noise, (adder, 0))
    #     tb.connect(adder, head)
    #     tb.connect(src, dst_src)
    #     tb.connect(noise, dst_noise)
    #     # tb.connect(head, fft)
    #     tb.connect(head, dst_input)
    #     # tb.connect(fft, snr)
    #     # tb.connect(snr, dst_out)

    #     tb.run()
    
    #     data_src = dst_src.data()
    #     data_noise = dst_noise.data()
    #     # data_input = dst_input.data()
    #     # data_out = dst_out.data()


    #     print 20*math.log10(np.var(data_src) / np.var(data_noise))






    def test_001_t (self):
        """test_001_t: sine wave"""
        tb = self.tb

        samp_rate = 100000
        items = samp_rate * 4 # 3 seconds of simulation

        dst_src = blocks.vector_sink_f()
        dst_noise = blocks.vector_sink_f()
        dst_input = blocks.vector_sink_f()
        dst_out = blocks.vector_sink_f()
        head = blocks.head(gr.sizeof_float, items)

        src = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 1024, 1, 0)
        noise = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)
        snr = flaress.snr(True, True, 1024, samp_rate, 1024, 10000,20000)
        adder = blocks.add_vff(1)
        fft = logpwrfft.logpwrfft_f(
        	sample_rate=samp_rate,
        	fft_size=1024,
        	ref_scale=2,
        	frame_rate=30,
        	avg_alpha=0.5,
        	average=False,
        )

        tb.connect(src, (adder, 1))
        tb.connect(noise, (adder, 0))
        tb.connect(adder, head)
        tb.connect(src, dst_src)
        tb.connect(noise, dst_noise)
        tb.connect(head, fft)
        tb.connect(head, dst_input)
        tb.connect(fft, snr)
        tb.connect(snr, dst_out)

        tb.run()
    
        data_src = dst_src.data()
        data_noise = dst_noise.data()
        data_input = dst_input.data()
        data_out = dst_out.data()


        print 10*math.log10(np.var(data_src) / np.var(data_noise))
        print np.mean(data_out)



if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_snr)
    runner = runner.HTMLTestRunner(output='Results',template='DEFAULT_TEMPLATE_1')
    runner.run(suite)
    gr_unittest.TestProgram()