#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks, analog
from gnuradio.fft import window
from gnuradio.filter import firdes
from collections import namedtuple
from gnuradio import filter
import flaress_swig as flaress
from snr_estimator_cf import snr_estimator_cf
from snr_estimator_cfv import snr_estimator_cfv
import runner, math
import numpy as np

def print_parameters(data):
    to_print = "/pr!Signal amplitude= %.2f V; Noise amplitude= %.2f V; f_samp= %.1f Hz; f_signal= %.1f Hz; Signal Bandwidth = %.1f Hz; Noise Bandwidth = %.1f Hz, FFT size = %d/pr!" \
        %(data.signal_amp, data.noise_amp, data.samp_rate, data.freq_sine, data.signal_bw, data.noise_bw, data.fft)
    print (to_print)


class qa_snr_estimator (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        """test_001_t: CNR with fixed noise bandwidth"""
        tb = self.tb

        param = namedtuple('param', 'signal_amp''noise_amp' 'samp_rate' 'freq_sine' 'signal_bw' 'noise_bw' 'fft')

        param.samp_rate = 32000
        items = param.samp_rate * 4 # 2 seconds of simulation
        param.signal_bw = 10
        param.noise_bw = 2000
        param.signal_amp = 1
        param.noise_amp = 1
        param.freq_sine = 2000
        param.fft = 4096

        print_parameters(param)

        dst_src = blocks.vector_sink_c()
        dst_noise = blocks.vector_sink_c()
        dst_noise_bw = blocks.vector_sink_c()
        dst_input = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_f()
        head1 = blocks.head(gr.sizeof_gr_complex, items)
        head2 = blocks.head(gr.sizeof_gr_complex, items)
        
        src = analog.sig_source_c(param.samp_rate, analog.GR_SIN_WAVE, param.freq_sine, param.signal_amp, 0)
        noise = analog.noise_source_c(analog.GR_GAUSSIAN, param.noise_amp, 0)
        
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)
        throttle2 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)

        bpf_signal = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.signal_bw/2), (param.freq_sine + param.signal_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        bpf_noise = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.noise_bw/2), (param.freq_sine + param.noise_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        snr = snr_estimator_cf(auto_carrier = True, carrier = True, all_spectrum = False, freq_central = param.freq_sine, samp_rate = param.samp_rate, nintems = param.fft, signal_bw = param.signal_bw , noise_bw = param.noise_bw, avg_alpha = 1.0, average = False, win = window.blackmanharris)
        
        adder = blocks.add_vcc(1)


        tb.connect(src, (adder, 1))
        tb.connect(noise, (adder, 0))
        tb.connect(src, bpf_signal)
        tb.connect(bpf_signal, dst_src)
        tb.connect(noise, bpf_noise)
        tb.connect(bpf_noise, dst_noise)
        tb.connect(adder, head1)
        tb.connect(head1, snr)
        tb.connect(snr, dst_out)
        
        tb.run()
    
        data_src = dst_src.data()
        data_noise = dst_noise.data()
        # data_input = dst_input.data()
        data_out = dst_out.data()


        print ("SNR evaluated with variance:",10*math.log10(np.var(data_src) / np.var(data_noise)))
        print ("SNR estimated:", np.mean(data_out))

    def test_002_t (self):
        """test_002_t: CNR with all spectrum"""
        tb = self.tb

        param = namedtuple('param', 'signal_amp''noise_amp' 'samp_rate' 'freq_sine' 'signal_bw' 'noise_bw' 'fft')

        param.samp_rate = 32000
        items = param.samp_rate * 4 # 2 seconds of simulation
        param.signal_bw = 10
        param.noise_bw = 2000
        param.signal_amp = 1
        param.noise_amp = 1
        param.freq_sine = 2000
        param.fft = 4096

        print_parameters(param)

        dst_src = blocks.vector_sink_c()
        dst_noise = blocks.vector_sink_c()
        dst_noise_bw = blocks.vector_sink_c()
        dst_input = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_f()
        head1 = blocks.head(gr.sizeof_gr_complex, items)
        head2 = blocks.head(gr.sizeof_gr_complex, items)
        
        src = analog.sig_source_c(param.samp_rate, analog.GR_SIN_WAVE, param.freq_sine, param.signal_amp, 0)
        noise = analog.noise_source_c(analog.GR_GAUSSIAN, param.noise_amp, 0)
        
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)
        throttle2 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)

        bpf_signal = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.signal_bw/2), (param.freq_sine + param.signal_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        bpf_noise = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.noise_bw/2), (param.freq_sine + param.noise_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        snr = snr_estimator_cf(auto_carrier = True, carrier = True, all_spectrum = True, freq_central = param.freq_sine, samp_rate = param.samp_rate, nintems = param.fft, signal_bw = param.signal_bw , noise_bw = param.noise_bw, avg_alpha = 1.0, average = False, win = window.blackmanharris)
        
        adder = blocks.add_vcc(1)


        tb.connect(src, (adder, 1))
        tb.connect(noise, (adder, 0))
        tb.connect(src, dst_src)
        tb.connect(noise, dst_noise)
        tb.connect(adder, head1)
        tb.connect(head1, snr)
        tb.connect(snr, dst_out)
        
        tb.run()
    
        data_src = dst_src.data()
        data_noise = dst_noise.data()
        # data_input = dst_input.data()
        data_out = dst_out.data()


        print ("SNR evaluated variance:",10*math.log10(np.var(data_src) / np.var(data_noise)))
        print ("SNR estimated:", np.mean(data_out))

    def test_003_t (self):
        """test_003_t: SNR with fixed noise bandwidth"""
        tb = self.tb

        param = namedtuple('param', 'signal_amp''noise_amp' 'samp_rate' 'freq_sine' 'signal_bw' 'noise_bw' 'fft')

        param.samp_rate = 32000
        items = param.samp_rate * 4 # 2 seconds of simulation
        param.signal_bw = 200
        param.noise_bw = 2000
        param.signal_amp = 1
        param.noise_amp = 1
        param.freq_sine = 2000
        param.fft = 4096

        print_parameters(param)

        dst_src = blocks.vector_sink_c()
        dst_noise = blocks.vector_sink_c()
        dst_noise_bw = blocks.vector_sink_c()
        dst_input = blocks.vector_sink_c()
        dst_out = blocks.vector_sink_f()
        head1 = blocks.head(gr.sizeof_gr_complex, items)
        head2 = blocks.head(gr.sizeof_gr_complex, items)
        
        src = analog.sig_source_c(param.samp_rate, analog.GR_SIN_WAVE, param.freq_sine, param.signal_amp, 0)
        noise = analog.noise_source_c(analog.GR_GAUSSIAN, param.noise_amp, 0)
        
        throttle1 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)
        throttle2 = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)

        bpf_signal = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.signal_bw/2), (param.freq_sine + param.signal_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        bpf_noise = filter.fir_filter_ccc(1, firdes.complex_band_pass(1, param.samp_rate, (param.freq_sine - param.noise_bw/2), (param.freq_sine + param.noise_bw/2), 1, firdes.WIN_HAMMING, 6.76))
        
        snr = snr_estimator_cf(auto_carrier = True, carrier = False, all_spectrum = False, freq_central = param.freq_sine, samp_rate = param.samp_rate, nintems = param.fft, signal_bw = param.signal_bw , noise_bw = param.noise_bw, avg_alpha = 1.0, average = False, win = window.blackmanharris)
        
        adder = blocks.add_vcc(1)


        tb.connect(src, (adder, 1))
        tb.connect(noise, (adder, 0))
        tb.connect(src, bpf_signal)
        tb.connect(bpf_signal, dst_src)
        tb.connect(noise, bpf_noise)
        tb.connect(bpf_noise, dst_noise)
        tb.connect(adder, head1)
        tb.connect(head1, snr)
        tb.connect(snr, dst_out)
        
        tb.run()
    
        data_src = dst_src.data()
        data_noise = dst_noise.data()
        # data_input = dst_input.data()
        data_out = dst_out.data()


        print ("SNR evaluated variance:",10*math.log10(np.var(data_src) / np.var(data_noise)))
        print ("SNR estimated:", np.mean(data_out))

if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_snr_estimator)
    runner = runner.HTMLTestRunner(output='../TestResults',template='DEFAULT_TEMPLATE_2')
    runner.run(suite)
    #gr_unittest.TestProgram()