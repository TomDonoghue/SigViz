"""Model related plot functions."""

import numpy as np

from neurodsp.plts.utils import check_ax

from fooof.sim.gen import gen_aperiodic
from fooof.plts.fm import _add_peaks_shade

from vcode.plts.timeseries import plot_spectra

from vcode.settings.bands import BANDS, COLORS
#from vcode.settings.models import F_RANGE, YLIM
#from vcode.settings.models import YLIM

###################################################################################################
###################################################################################################

## POWER SPECTRA

def plot_model_spectrum(model, freqs, powers, ax, **kwargs):

    funcs = {
        'freq' : plot_spectra_freq,
        'band' : plot_spectra_band,
        'peap' : plot_spectra_peap
    }

    funcs[model](freqs, powers, **kwargs, ax=ax)

def plot_spectra_freq(freqs, powers, ax=None, **kwargs):

    ax = check_ax(ax)
    plot_spectra(freqs, powers,
                 marker='.', linestyle="",
                 xlim=kwargs.get('xlim', None),
                 ylim=kwargs.get('ylim', None),
                 colors='blue', alpha=0.65, ms=12, ax=ax)
    plot_spectra(freqs, powers,
                 xlim=kwargs.get('xlim', None),
                 ylim=kwargs.get('ylim', None),
                 colors='black', alpha=0.35, lw=1.5, ax=ax)

def plot_spectra_band(freqs, powers, ax=None, **kwargs):

    ax = check_ax(ax)
    plot_spectra(freqs, powers,
                 shade_ranges=BANDS.definitions,
                 shade_colors=list(COLORS.values()),
                 xlim=kwargs.get('xlim', None),
                 ylim=kwargs.get('ylim', None),
                 colors='black', alpha=0.75, ax=ax)

def plot_spectra_peap(freqs, powers, fm, ax=None, **kwargs):

    ax = check_ax(ax)
    plot_spectra(freqs, powers,
                 xlim=kwargs.get('xlim', None),
                 ylim=kwargs.get('ylim', None),
                 colors='black', alpha=0.75, ax=ax)

    ap_fit = gen_aperiodic(freqs, fm.aperiodic_params_)
    #ax.plot(np.log10(freqs), FM.fooofed_spectrum_, color='red', alpha=0.5)
    ax.plot(np.log10(freqs), ap_fit, '--', c='blue', lw=2.5, alpha=0.75)
    if fm.n_peaks_:
        _add_peaks_shade(fm, True, ax)


## TEXT

def add_model_text(model, ax=None):

    ax = check_ax(ax)
    fontdict = {'fontsize' : 24}

    texts = {
        'freq' : 'Frequency\nby\nFrequency',
        'band' : 'Band\nby\nBand',
        'peap' : 'Periodic\n&\nAperiodic'
    }

    ax.text(0.5, 0.85, "Model:",
            fontdict=fontdict, ha='center')
    ax.text(0.5, 0.35, texts[model],
            fontdict=fontdict, ha='center')
    ax.axis('off')
