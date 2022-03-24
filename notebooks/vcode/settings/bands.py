""""Band related settings."""

from fooof import Bands

###################################################################################################
###################################################################################################

BANDS = Bands({
    'delta' : [1, 4],
    'theta' : [4, 8],
    'alpha' : [8, 13],
    'beta' : [13, 30],
    'gamma' : [30, 50]
})

COLORS = {
    'delta' : '#e8dc35',
    'theta' : '#46b870',
    'alpha' : '#1882d9',
    'beta'  : '#a218d9',
    'gamma' : '#e60026'}

LABELS = {
    'delta' : r'$\delta$',
    'theta' : r'$\theta$',
    'alpha' : r'$\alpha$',
    'beta'  : r'$\beta$',
    'gamma' : r'$\gamma$'
}
