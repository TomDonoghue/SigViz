"""Base plots."""

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
