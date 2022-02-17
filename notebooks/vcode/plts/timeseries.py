"""Timeseries plot functions."""

import warnings
from itertools import repeat

import numpy as np

from neurodsp.plts.utils import check_ax

###################################################################################################
###################################################################################################

def plot_timeseries(signals, shade=None, colors=None, xlim=None, ylim=None,
                    offset=0, ax=None, **plt_kwargs):
    """Plot time series."""

    ax = check_ax(ax)

    if isinstance(signals, np.ndarray):
        signals = [signals]

    if isinstance(colors, str) or colors is None:
        colors = repeat(colors)

    for ind, (signal, color) in enumerate(zip(signals, colors)):
        ax.plot(signal + ind * offset, color=color, **plt_kwargs)

    if xlim:
        ax.set_xlim(xlim)
    else:
        # Despite seeming like this redundantly resets the limits to what they already are,
        #   for some reason this seems to make sure that shading goes the full length
        ax.set_xlim(*ax.get_xlim())

    if ylim:
        ax.set_ylim(ylim)

    if shade:
        ax.axvspan(*ax.get_xlim(), alpha=0.2, color=shade)

    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None);


def plot_spectra(freqs, powers, log_freqs=True, log_powers=True, xlim=None, ylim=None,
                 colors=None, shade_ranges=None, shade_colors=None, ax=None, **plt_kwargs):
    """Plot power spectra."""

    ax = check_ax(ax)

    if isinstance(powers, np.ndarray):
        powers = [powers]

    if isinstance(colors, str) or colors is None:
        colors = repeat(colors)

    if log_freqs:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            freqs = np.log10(freqs)

    for power, color in zip(powers, colors):

        if log_powers:
            power = np.log10(power)

        ax.plot(freqs, power, color=color, **plt_kwargs)

    if shade_ranges:
        add_shades(ax, shade_ranges, shade_colors, logged=log_freqs)

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    ax.set(xticks=[], yticks=[], xlabel=None, ylabel=None);
