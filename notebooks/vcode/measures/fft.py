"""Functions for computing FFT measures."""

import cmath

import numpy as np

###################################################################################################
###################################################################################################

def decompose_fft(data, threshold=0., max_n_waves=np.inf):
    """Decompose the components of an FFT.

    Parameters
    ----------
    data, threshold, max_n_waves

    Returns
    -------
    sines, freqs, phases, powers

    Notes
    -----
    Adapted from:
    https://stackoverflow.com/questions/59725933/plot-fft-as-a-set-of-sine-waves-in-python
    """

    fft3 = np.fft.fft(data)
    x = np.arange(0, 10, 10 / len(data))
    freqs = np.fft.fftfreq(len(x), .01)

    sines = np.empty([0, len(x)])
    phases = []
    powers = []

    for ind in range(len(fft3)):

        if ind > max_n_waves:
            break

        power = abs(fft3[ind])
        phase = cmath.phase(fft3[ind])
        coeff = 2 if ind == 0 else 1

        if power / len(x) > threshold:

            sinewave = 1/(len(x)*coeff/2) * \
                (power * np.cos(freqs[ind]*2*np.pi*x+phase))

            sines = np.vstack([sines, sinewave])

            phases.append(phase)
            powers.append(power)

    return sines, freqs, phases, powers
