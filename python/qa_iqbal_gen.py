#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Antonio Miraglia - ISISpace .
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks, channels, analog
from collections import namedtuple
from scipy import signal
import flaress_swig as flaress
import math, time, datetime
import numpy as np
import runner, os, abc, sys, pmt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Pdf_class(object):
    """this class can print a single pdf for all the tests"""

    graphs_list = []

    def __init__(self, name_test='test'):
        current_dir = os.getcwd()
        dir_to = os.path.join(current_dir, 'Graphs')

        if not os.path.exists(dir_to):
            os.makedirs(dir_to)
        self.name_test = name_test.split('.')[0]
        self.name_complete = dir_to + '/' + name_test.split('.')[0] + "_graphs.pdf"

    def add_to_pdf(self, fig):
        """this function can add a new element/page to the list of pages"""

        fig_size = [21 / 2.54, 29.7 / 2.54] # width in inches & height in inches
        fig.set_size_inches(fig_size)
        Pdf_class.graphs_list.append(fig)

    def finalize_pdf(self):
        """this function print the final version of the pdf with all the pages"""

        with PdfPages(self.name_complete) as pdf:
            for graph in Pdf_class.graphs_list:
                pdf.savefig(graph)   #write the figures for that list

            d = pdf.infodict()
            d['Title'] = self.name_test
            d['Author'] = 'Antonio Miraglia - ISISpace'
            d['Subject'] = 'self generated graphs from the qa test'
            d['Keywords'] = self.name_test
            d['CreationDate'] = datetime.datetime(2018, 8, 21)
            d['ModDate'] = datetime.datetime.today()

def print_parameters(data):
    to_print = "\p Sample rate = %d Hz; Input Frequency = %.3f Hz; Input Amplitude = %.3f V; Input Offset =  %.3f V; Magnitude Imbalance  = %d; Phase Imbalance = %f; Origin = %s \p" \
        %(data.samp_rate, data.frequency, data.amplitude, data.offset, data.magnitude, data.phase, data.origin)
    print to_print

def plot(self, data):
    """this function create a defined graph for the pll with the data input and output"""

    plt.rcParams['text.usetex'] = True
    out_real = []
    out_imag = []
    in_real = []
    in_imag = []


    print data.corr


    for i in xrange (len(data.out)):
        out_real.append(data.out[i].real)
        out_imag.append(data.out[i].imag)
    
    for i in xrange (len(data.src)):
        in_real.append(data.src[i].real)
        in_imag.append(data.src[i].imag)

    out_re = np.asarray(out_real)
    out_im = np.asarray(out_imag)
    in_re = np.asarray(in_real)
    in_im = np.asarray(in_imag)
    corr = np.asarray(data.corr)
    time = np.asarray(data.time)
    time_corr = np.asarray(data.time_corr)

    fig, (ax1, ax3, ax5) = plt.subplots(3)

    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel ('Real', color='r')
    ax1.set_title("Input", fontsize=20)
    ax1.set_xlim([0.0, 0.04])
    ax1.plot(time, in_re, color='r', scalex=True, scaley=True, linewidth=1)
    ax1.tick_params(axis='y', labelcolor='red')
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.set_ylabel('Imag', color='b')  # we already handled the x-label with ax1
    ax2.set_xlim([0.0, 0.04])
    ax2.plot(time, in_im, color='b', scalex=True, scaley=True, linewidth=1)
    ax2.tick_params(axis='y', labelcolor='blue')

    ax3.set_xlabel('Time [s]')
    ax3.set_ylabel ('Real', color='r')
    ax3.set_title("Output", fontsize=20)
    ax3.set_xlim([0.0, 0.04])
    ax3.plot(time, out_re, color='r', scalex=True, scaley=True, linewidth=1)
    ax3.tick_params(axis='y', labelcolor='red')
    ax3.grid(True)

    ax4 = ax3.twinx()
    ax4.set_ylabel('Imag', color='b')  # we already handled the x-label with ax1
    ax4.set_xlim([0.0, 0.04])
    ax4.plot(time, out_im, color='b', scalex=True, scaley=True, linewidth=1)
    ax4.tick_params(axis='y', labelcolor='blue')


    ax5.set_xlabel('Item')
    ax5.set_ylabel ('Real', color='r')
    ax5.set_title("Cross-correlation", fontsize=20)
    ax5.axhline(0.5, ls=':')
    ax5.axvline(len(corr.real)/2, ls=':')
    # ax5.set_ylim([-0.1, 1.1])
    ax5.set_xlim([1850, 2250])
    ax5.plot(corr.real, color='r', scalex=True, scaley=True, linewidth=1)
    # ax5.plot(time_corr, corr.real, color='r', scalex=True, scaley=True, linewidth=1)
    ax5.tick_params(axis='y', labelcolor='red')
    ax5.grid(True)

    ax6 = ax5.twinx()
    ax6.set_ylabel('Imag', color='b')  # we already handled the x-label with ax1
    ax6.set_xlim([1850, 2250])
    ax6.plot(corr.imag, color='b', scalex=True, scaley=True, linewidth=1)
    # ax6.plot(time_corr, corr.imag, color='b', scalex=True, scaley=True, linewidth=1)
    ax6.tick_params(axis='y', labelcolor='blue')

    name_test = self.id().split("__main__.")[1]
    name_test_usetex = name_test.replace('_', '\_').replace('.', ': ')

    fig.suptitle(name_test_usetex, fontsize=30)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    fig.subplots_adjust(hspace=0.6, top=0.85, bottom=0.15)

    # plt.show()
    self.pdf.add_to_pdf(fig)


def test_imbalance(self, param):
    """this function run the defined test, for easier understanding"""

    tb = self.tb
    data = namedtuple('data_pc', 'src out corr time time_corr')

    src_sine = analog.sig_source_c(param.samp_rate, analog.GR_SIN_WAVE, param.frequency, param.amplitude, param.offset)

    throttle = blocks.throttle(gr.sizeof_gr_complex*1, param.samp_rate,True)
    head = blocks.head(gr.sizeof_gr_complex, int (param.items))

    if param.origin == "TX":
        iqbal = channels.iqbal_gen(param.magnitude, param.phase, 0)
    else:
        iqbal = channels.iqbal_gen(param.magnitude, param.phase, 1)

    dst_src = blocks.vector_sink_c()
    dst_out = blocks.vector_sink_c()

    tb.connect(src_sine, throttle)
    tb.connect(throttle, head)
    tb.connect(head, dst_src)
    tb.connect(head, iqbal)
    tb.connect(iqbal, dst_out)

    self.tb.run()

    data.src = dst_src.data()
    data.out = dst_out.data()
    data.time = np.linspace(0, (param.items * 1.0 / param.samp_rate), param.items, endpoint=False)

    data.corr = signal.correlate(data.out, data.src) / param.items

    data.time_corr = np.linspace(-(param.items * 1.0 / param.samp_rate), (param.items * 1.0 / param.samp_rate), len(data.corr), endpoint=True)
    return data

class qa_iqbal_gen (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()
        self.pdf = Pdf_class(self.id().split(".")[1])

    def tearDown (self):
        self.tb = None
        self.pdf.finalize_pdf()

    def test_001_t (self):
        """test_001_t: without imbalance"""
        param = namedtuple('param', 'samp_rate items frequency amplitude offset magnitude phase origin')
        param.samp_rate = 2048
        param.items = param.samp_rate
        param.frequency = 50.0
        param.amplitude = 1.0
        param.offset = 0.0
        param.magnitude = 0.0
        param.phase = 0.0
        param.origin = "TX"

        print_parameters(param)

        data = test_imbalance(self, param)

        plot(self,data)

        # i,j = np.unravel_index(data.corr.argmax(), data.corr.shape) #get the index of the maximum value of correlation
        # # self.assertAlmostEqual(param.step / (2 * math.pi), data_fft.carrier)
        # print "Time shifting= %.3f ms;" %(data.time_corr[i]*1000)

    def test_002_t (self):
        """test_002_t: with imbalance"""
        param = namedtuple('param', 'samp_rate items frequency amplitude offset magnitude phase origin')
        param.samp_rate = 2048
        param.items = param.samp_rate
        param.frequency = 50.0
        param.amplitude = 1.0
        param.offset = 0.0
        param.magnitude = 10.0
        param.phase = -10.0
        param.origin = "TX"

        print_parameters(param)

        data = test_imbalance(self, param)

        plot(self,data)

        # i,j = np.unravel_index(data.corr.argmax(), data.corr.shape) #get the index of the maximum value of correlation
        # # self.assertAlmostEqual(param.step / (2 * math.pi), data_fft.carrier)
        # print "Time shifting= %.3f ms;" %(data.time_corr[i]*1000)

if __name__ == '__main__':
    suite = gr_unittest.TestLoader().loadTestsFromTestCase(qa_iqbal_gen)
    runner = runner.HTMLTestRunner(output='Results', template='DEFAULT_TEMPLATE_2')
    runner.run(suite)
    #gr_unittest.TestProgram()