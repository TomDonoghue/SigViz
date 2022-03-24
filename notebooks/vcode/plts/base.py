"""Base plots."""

import matplotlib.pyplot as plt

from neurodsp.plts.utils import check_ax

###################################################################################################
###################################################################################################

def plot_data(x_values=None, y_values=None, ax=None, **kwargs):
    """Generic plot for plotting data."""

    ax = check_ax(ax, [5, 5])

    if y_values is None:
        ax.plot(x_values, **kwargs)
    else:
        ax.plot(x_values, y_values, **kwargs)


def plot_table(table_data, ax=None):
    """Generic plot for plotting a table."""

    ax = check_ax(ax)

    table = plt.table(table_data, colWidths=[0.5, 0.5],
                      loc='center', cellLoc='center')
    table.set_fontsize(20)
    table.scale(1, 3.75)
    ax.axis('off')
