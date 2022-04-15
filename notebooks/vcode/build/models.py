"""Builder functions for the model visualizers."""

import numpy as np
import matplotlib.pyplot as plt

from neurodsp.spectral import compute_spectrum, trim_spectrum

from vcode.plts.base import plot_table
from vcode.plts.settings import TITLE_FD
from vcode.plts.timeseries import plot_timeseries
from vcode.plts.utils import clear_output, animate_plot
from vcode.plts.models import plot_model_spectrum, add_model_text

from vcode.utils.data import yield_sig
from vcode.measures.models import get_features
from vcode.measures.spectra import fit_specparam

###################################################################################################
###################################################################################################

### AXES

def make_axes_model():
    """Make axes for combined plot."""

    fig = plt.figure()
    ax1 = fig.add_axes([0.0, 1.15, 0.5, 0.55])
    ax2 = fig.add_axes([0.5, 1.3, 1.4, 0.35])

    ax3 = fig.add_axes([0.0, 0.3, 0.5, 0.7])
    ax4 = fig.add_axes([0.6, 0.3, 0.7, 0.8])
    ax5 = fig.add_axes([1.4, 0.3, 0.5, 0.8])

    return fig, [ax1, ax2, ax3, ax4, ax5]

## THIS WAS FOR A SMALLER PLOT SIZE
# def make_axes_model():

#     fig = plt.figure()
#     ax1 = fig.add_axes([0.0, 1.1, 0.4, 0.5])
#     ax2 = fig.add_axes([0.4, 1.25, 1.1, 0.3])

#     ax3 = fig.add_axes([0.0, 0.5, 0.4, 0.5])
#     ax4 = fig.add_axes([0.5, 0.5, 0.6, 0.65])
#     ax5 = fig.add_axes([1.2, 0.5, 0.3, 0.65])

#     return fig, [ax1, ax2, ax3, ax4, ax5]


### BUILDERS

def build_model(sig, fs, model, img, f_range=[2, 50], sparam={}, n_build=np.inf,
                sleep=0.05, save=False, label='model', **kwargs):
    """Build all plots together."""

    # Step settings
    start = 1000
    size = 1000
    step = 3

    feat_kwargs = {}

    sig_yielder = yield_sig(sig, start=start, size=size, step=step)

    for ind in range(n_build):

        clear_output(wait=True)

        fig, axes = make_axes_model()

        # Default plot kwargs, if not provided
        kwargs.setdefault('xlim', f_range)

        # Compute needed things
        spect_sig = sig[start + step * ind-size:start + step * ind+size]
        freqs, powers = trim_spectrum(*compute_spectrum(spect_sig, fs=fs), f_range)

        if model == 'peap':
            feat_kwargs['fm'] = fit_specparam(freqs, powers, **sparam)

        # Axis 0
        axes[0].imshow(img)
        axes[0].axis('off')

        # Axis 1
        plot_timeseries(next(sig_yielder), colors='black',
                        lw=1.75, alpha=0.75, ax=axes[1])
        axes[1].axis('off')

        # Axis 2
        add_model_text(model, ax=axes[2])

        # Axis 3
        plot_model_spectrum(model, freqs, powers, ax=axes[3], **{**kwargs, **feat_kwargs})
        axes[3].set_title('Spectral Representation', fontdict=TITLE_FD)

        # Axis 4
        table_data = get_features(model, freqs, powers, **feat_kwargs)
        plot_table(table_data, ax=axes[4])
        axes[4].set_title('Features', fontdict=TITLE_FD)

        animate_plot(fig, save, ind, label=label, sleep=sleep)
