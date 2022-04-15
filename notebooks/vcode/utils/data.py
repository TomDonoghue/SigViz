"""Utility functions."""

import numpy as np

###################################################################################################
###################################################################################################

def yield_sig(sig, start=0, size=100, step=1):
    """Helper function to yield segments of a signal."""

    for st in range(start, len(sig)-size, step):
        yield sig[st:st+size]


def find_nearest_ind(array, value):
    """Find the index closest to a provided value."""

    return np.abs(array-value).argmin()


def incrementer(start=0, end=999):
    """Generator that returns an incrementing index value.

    Parameters
    ----------
    start, end : int
        The start and end point for the incrementer.

    Yields
    ------
    ind : int
        The current index value.
    """

    for ind in range(start, end):
        yield ind
