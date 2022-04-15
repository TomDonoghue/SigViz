"""FFT plot functions."""

import numpy as np
import matplotlib.pyplot as plt

from .settings import COLORS_LST

###################################################################################################
###################################################################################################

def plot_sines(sines, ax=None):
    """Plot individual sine waves."""

    if not ax:
        _, ax = plt.subplots()

    for sine in sines:
        ax.plot(sine, alpha=0.5)

    ax.set(xticks=[], yticks=[])


def plot_recomb(sines, data, ax=None):
    """Plot recombined sine waves."""

    if not ax:
        _, ax = plt.subplots()

    ax.plot(np.sum(sines, 0), color='red')
    if np.any(data):
        ax.plot(data, color='black')
        ax.set_ylim([np.min(data)-0.25 , np.max(data)+0.25])

    ax.set(xticks=[], yticks=[])


def plot_phases(phases, ax=None):
    """Plot phase distribution."""

    if not ax:
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

    for phase in phases:
        ax.plot([0, phase], [0, 1], lw=4, alpha=0.5)

    ax.set(xticklabels=[], yticklabels=[])


def plot_powers(freqs, powers, log_powers=False, ax=None):
    """Plot power distribution."""

    if not ax:
        _, ax = plt.subplots(figsize=(5, 5))

    if log_powers:
        powers = np.log10(powers)

    ax.scatter(freqs, powers, c=COLORS_LST[0:len(freqs)])
    ax.set(xticks=[], yticks=[])
