"""Builder functions for filters."""

import matplotlib.pyplot as plt

from neurodsp.filt.fir import design_fir_filter
from neurodsp.filt.utils import compute_frequency_response
from neurodsp.plts.filt import plot_frequency_response, plot_impulse_response

from vcode.utils.data import incrementer
from vcode.plts.filt import add_filter_text
from vcode.plts.utils import clear_output, animate_plot, passer

###################################################################################################
###################################################################################################

### AXES

def make_axes_filter_properties():
    """Make axes for combined plot."""

    fig = plt.figure()
    ax1 = fig.add_axes([0.0, 0.8, 0.15, 0.75])
    ax1.axis('off')
    ax2 = fig.add_axes([0.35, 0.8, 0.75, 0.75])
    ax3 = fig.add_axes([1.3, 0.8, 0.75, 0.75])

    return fig, [ax1, ax2, ax3]


### BUILDERS

def build_filter_properties(fs, pass_type, f_range, n_cycles, field, values,
                            fr_xlim=[0, 150], fr_ylim=[-100, 0], imp_xlim=None, imp_ylim=None,
                            sleep=0.05, save=False, label='filter_properties'):
    """Build function for filter properties."""

    if field == 'bandwidth':
        cen = f_range

    inc = incrementer()
    for value in values:

        if field == 'f_range':
            f_range = value
        if field == 'n_cycles':
            n_cycles = value
        if field == 'bandwidth':
            f_range = (cen-value, cen+value)

        filt_coefs = design_fir_filter(fs, pass_type, f_range, n_cycles)
        f_db, db = compute_frequency_response(filt_coefs, 1, fs)

        clear_output(wait=True)

        fig, axes = make_axes_filter_properties()
        add_filter_text(axes[0], pass_type, f_range, n_cycles)
        plot_frequency_response(f_db, db, ax=axes[1],
                                xlim=fr_xlim, ylim=fr_ylim,
                                custom_styler=passer)
        plot_impulse_response(fs, filt_coefs, ax=axes[2],
                              xlim=imp_xlim, ylim=imp_ylim,
                              custom_styler=passer)

        animate_plot(fig, save, next(inc), label=label, sleep=sleep)
