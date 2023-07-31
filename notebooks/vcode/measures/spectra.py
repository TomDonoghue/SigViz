"""Power spectra related measures."""

import numpy as np

from neurodsp.spectral import trim_spectrum

###################################################################################################
###################################################################################################

def compute_abs_power(freqs, powers, band):
    """Compute absolute power for a given frequency band."""

    _, band_powers = trim_spectrum(freqs, powers, band)
    avg_power = np.sum(band_powers)

    return avg_power
