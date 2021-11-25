#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Carrier Sweep
# Author: stefanosperett
# GNU Radio version: 3.8.4.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class carrier_sweep(gr.top_block, Qt.QWidget):

    def __init__(self, samp_rate=32000):
        gr.top_block.__init__(self, "Carrier Sweep")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Carrier Sweep")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "carrier_sweep")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.sweep_rate = sweep_rate = 2000
        self.sweep_range = sweep_range = 8000
        self.subcarrier = subcarrier = 16000
        self.snr = snr = 20
        self.modulation_coeff = modulation_coeff = 0.1
        self.frequency = frequency = 2000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, 1, 1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.analog_sig_source_x_2_1 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, 0 if sweep_range == 0 else sweep_rate/sweep_range, 2*3.14159265359*sweep_range, 2*3.14159265359*frequency, -3.14159265359)
        self.analog_sig_source_x_2_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, subcarrier, modulation_coeff, 0, 0)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 10**(-snr/10), 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_2_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.analog_sig_source_x_2_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "carrier_sweep")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_sweep_rate(self):
        return self.sweep_rate

    def set_sweep_rate(self, sweep_rate):
        self.sweep_rate = sweep_rate
        self.analog_sig_source_x_2_1.set_frequency(0 if self.sweep_range == 0 else self.sweep_rate/self.sweep_range)

    def get_sweep_range(self):
        return self.sweep_range

    def set_sweep_range(self, sweep_range):
        self.sweep_range = sweep_range
        self.analog_sig_source_x_2_1.set_frequency(0 if self.sweep_range == 0 else self.sweep_rate/self.sweep_range)
        self.analog_sig_source_x_2_1.set_amplitude(2*3.14159265359*self.sweep_range)

    def get_subcarrier(self):
        return self.subcarrier

    def set_subcarrier(self, subcarrier):
        self.subcarrier = subcarrier
        self.analog_sig_source_x_2_0.set_frequency(self.subcarrier)

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr
        self.analog_noise_source_x_0.set_amplitude(10**(-self.snr/10))

    def get_modulation_coeff(self):
        return self.modulation_coeff

    def set_modulation_coeff(self, modulation_coeff):
        self.modulation_coeff = modulation_coeff
        self.analog_sig_source_x_2_0.set_amplitude(self.modulation_coeff)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_2_1.set_offset(2*3.14159265359*self.frequency)




def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--samp-rate", dest="samp_rate", type=intx, default=32000,
        help="Set Sample Rate (sps) [default=%(default)r]")
    return parser


def main(top_block_cls=carrier_sweep, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(samp_rate=options.samp_rate)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
