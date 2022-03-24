"""Utility functions for creating plotting / gifs."""

from IPython.display import clear_output

import time

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

def animate_plot(fig, save, build_ind, label='fig', sleep=0.01, folder='outputs'):
    """Helper function for showing and/or saving out gif images.
    Notes: if set to save, the plot is not displayed.
    """

    if save:
        fig.savefig(folder + '/' + label + '/gif_' + str(build_ind) + '.jpg',
                    bbox_inches="tight", dpi=600, transparent=False)
        plt.close()
    else:
        plt.show();
        time.sleep(sleep)
