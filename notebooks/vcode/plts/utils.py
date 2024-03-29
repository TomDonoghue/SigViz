"""Utility functions for creating plotting / gifs."""

import os
import time
from pathlib import Path

from IPython.display import clear_output

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

def animate_plot(fig, save, build_ind, label='fig', sleep=0.01, folder='outputs'):
    """Helper function for showing and/or saving out gif images.
    Notes: if set to save, the plot is not displayed.
    """

    output_path = Path(folder) / label
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if save:
        fig.savefig(output_path / ('gif_' + str(build_ind) + '.jpg'),
                    bbox_inches="tight", dpi=600, transparent=False)
        plt.close()
    else:
        plt.show()
        time.sleep(sleep)


def passer(*args, **kwargs):
    """Helper function to pass through for custom styling."""
    pass
