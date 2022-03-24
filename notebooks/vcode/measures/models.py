"""Functions for computing model related measures."""

import numpy as np

from fooof.analysis import get_band_peak_fm

from vcode.utils.data import find_nearest_ind
from vcode.measures.spectra import compute_abs_power
from vcode.settings.bands import BANDS, LABELS

###################################################################################################
###################################################################################################

## FEATURES

def get_features(model, freqs, powers, **kwargs):

    funcs = {
        'freq' : get_features_freq,
        'band' : get_features_band,
        'peap' : get_features_peap,
    }

    return funcs[model](freqs, powers, **kwargs)

def get_features_freq(freqs, powers):

    extract = np.array([5, 10, 15, 20, 25])
    values = [powers[find_nearest_ind(freqs, freq)] for freq in extract]

    c1 = ['freq-{}'.format(val) for val in extract]
    c2 = ['{:1.3f}'.format(val) for val in values]
    col_data = [[a, b] for a, b in zip(c1, c2)]

    return col_data

def get_features_band(freqs, powers):

    powers = [compute_abs_power(freqs, powers, band) for band in BANDS.definitions]
    powers = ['{:1.3f}'.format(val) for val in powers]
    col_data = [[a, b] for a, b in zip(LABELS.values(), powers)]

    return col_data

def get_features_peap(freqs, powers, fm):

    exp = fm.get_params('aperiodic', 'exponent')
    off = fm.get_params('aperiodic', 'offset')

    alpha = get_band_peak_fm(fm, BANDS['alpha'])
    if np.isnan(alpha[0]):
        alpha = [0, 0, 0]
    cf, pw, bw = alpha

    labels = ['ap-exp', 'ap-off', r'$\alpha$-cf', r'$\alpha$-pw', r'$\alpha$-bw']
    values = ['{:1.3f}'.format(val) for val in [exp, off, cf, pw, bw]]

    col_data = [[a, b] for a, b in zip(labels, values)]

    return col_data
