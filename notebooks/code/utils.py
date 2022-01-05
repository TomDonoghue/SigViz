"""Utility functions."""

import numpy as np

###################################################################################################
###################################################################################################

def yield_sig(sig, start=0, size=100, step=1):
    """Helper function to yield segments of a signal."""

    for st in range(start, len(sig)-size, step):
        yield sig[st:st+size]
