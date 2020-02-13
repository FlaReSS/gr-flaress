#!/usr/bin/env python

from gnuradio import gr
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio import filter
import flaress
import sys, math


class snr_estimator_cfv(gr.hier_block2):
    """
    Estimates the SNR with complex input.
    """
    def __init__(self, auto_carrier, carrier, all_spectrum, freq_central, samp_rate, nintems, signal_bw, noise_bw, avg_alpha, average, win):
        """
        Estimates the SNR.
        Provide access to the setting the filter and sample rate.

        Args:
            sample_rate: Incoming stream sample rate
            nintems: Number of FFT bins
            avg_alpha: FFT averaging (over time) constant [0.0-1.0]
            average: Whether to average [True, False]
            win: the window taps generation function
            auto_carrier: To allow self-detection of the carrier, so the highest bin [True, False]
            carrier: To evalutaion of the CNR or SNR [True, False]
            all_spectrum: To set the whole spectrum (less the signal's one) to evaluate noise power density [True, False]
            freq_central: Sets the central frequency (for the bandwidth) of the signal (in the CNR mode, it is the manual set of the carrier's frequency)
            signal_bw: Sets the bandwidth (for the SNR mode) of the signal to the power evaluation
            noise_bw: Sets the bandwidth (if all_sepctrum is false) of the noise to the power evaluation
        """
        gr.hier_block2.__init__(self, "snr_estimator_cfv",
            gr.io_signature(1,1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature2(2,2, gr.sizeof_float, gr.sizeof_float * nintems)) # Output signature


        self.auto_carrier = auto_carrier
        self.carrier = carrier
        self.all_spectrum = all_spectrum
        self.freq_central = freq_central
        self.samp_rate = samp_rate
        self.nintems = nintems
        self.signal_bw = signal_bw
        self.noise_bw = noise_bw
        self.avg_alpha = avg_alpha
        self.average = average
        self.win = win



        fft_window = self.win(self.nintems)

        self.fft = fft.fft_vcc(self.nintems, True, fft_window, True)

        self._sd = blocks.stream_to_vector(gr.sizeof_gr_complex, self.nintems)
        self.c2magsq = blocks.complex_to_mag_squared(self.nintems)
        self._avg = filter.single_pole_iir_filter_ff(1.0, self.nintems)

        self.snr = flaress.snr(self.auto_carrier, self.carrier, self.all_spectrum, self.freq_central, self.samp_rate, self.nintems, self.signal_bw, self.noise_bw)

        window_power = sum(map(lambda x: x*x, fft_window))
        self.log = blocks.nlog10_ff(10, self.nintems,
                                     -20*math.log10(self.nintems)              # Adjust for number of bins
                                     -10*math.log10(float(window_power)/self.nintems) # Adjust for windowing loss
                                     -20*math.log10(float(2)/2))      # Adjust for reference scale

        self.connect(self, self._sd, self.fft, self.c2magsq, self._avg, self.snr, (self, 0))
        self.connect(self._avg, self.log, (self, 1))

        self._average = average
        self._avg_alpha = avg_alpha
        self.set_avg_alpha(avg_alpha)
        self.set_average(average)


    def set_average(self, average):
        """
        Set the averaging filter on/off.

        Args:
            average: true to set averaging on
        """
        self._average = average
        if self._average:
            self._avg.set_taps(self._avg_alpha)
        else:
            self._avg.set_taps(1.0)

    def set_avg_alpha(self, avg_alpha):
        """
        Set the average alpha and set the taps if average was on.

        Args:
            avg_alpha: the new iir filter tap
        """
        self._avg_alpha = avg_alpha
        self.set_average(self._average)
