"""Filter plot functions."""

import numpy as np
import matplotlib.pyplot as plt

from .settings import TEXT_FONTDICT

###################################################################################################
###################################################################################################

## TEXT

def add_filter_text(ax, f_type=None, f_range=None, n_cycles=None):
    """Helper function to add text labels to filter properties plot."""

    ax.text(0.1, 0.85, "FIR\nFilter", TEXT_FONTDICT)
    ax.text(0.1, 0.55, "type:\n{}".format(f_type), TEXT_FONTDICT)
    ax.text(0.1, 0.25, "f_range:\n{}".format(str(f_range)), TEXT_FONTDICT)

    if n_cycles is not None:
        ax.text(0.1, 0.0, "n_cycles:\n{}".format(str(n_cycles)), TEXT_FONTDICT)
