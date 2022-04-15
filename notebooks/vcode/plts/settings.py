""""Plot settings."""

from itertools import cycle

import matplotlib.pyplot as plt

###################################################################################################
###################################################################################################

COLORS_DEF = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
COLORS_LST = [next(COLORS_DEF) for ind in range(10000)]

TITLE_FD = {'fontsize' : 22}

TEXT_FONTDICT = {'fontsize' : 15, 'fontname' : 'Verdana',
                 'ha' : 'center', 'linespacing' : 1.5}
