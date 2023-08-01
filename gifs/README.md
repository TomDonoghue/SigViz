# Signal Visualizer Gifs

This folder is a collection of visualizers created for exploration signal processing.

Re-use is allowed, following the included license.

## Visualizers

Visualizers are organized into different topics.

Note that the numbered labeling of the folders here matches the numbered labeling under `notebooks`,
indicating where each visualizer is created.

### 01-Timeseries

Timeseries visualizers include:
- `ts-osc`: time series, and associated power spectrum, of an oscillation
- `ts-white-noise`: time series, and associated power spectrum, of white noise
- `ts-pink-noise`: time series, and associated power spectrum, of pink noise
- `ts-brown-noise`: time series, and associated power spectrum, of brown noise
- `ts-comb`: time series, and associated power spectrum, of a combined signal, with an oscillation and pink noise
- `ts-comb-burst`: time series, and associated power spectrum, of a combined signal, with a bursty oscillation and pink noise

### 02-FFT

FFT visualizers include:
- `fft-aperiodic`: animated decomposition of the Fourier transform, applied to an aperiodic signal
- `fft-periodic`: animated decomposition of the Fourier transform, applied to a signal with a periodic component

### 03-Convolution

Convolution visualizers include:
- `convolution-short`: animated application of convolution, with a long kernel
- `convolution-long`: animated application of convolution, with a short kernel

### 04-Filters

Filter visualizers include:
- `filtconv-aperiodic`: animated application of convolving a filter kernel with an aperiodic time series
- `filtconv-combined`: animated application of convolving a filter kernel with a combined time series
- `filtconv-burst`: animated application of convolving a filter kernel with a burst time series
- `filtconv-burst`: animated application of convolving a filter kernel with a step function time series
- `filtout-step-bandwidth`: animated showing a filter, an input step function, and output, across different bandwidths
- `filtout-step-ncycles`: animated showing a filter, an input step function, and output, across different n_cycles
- `filtparam-bandwidth`: animation showing filter properties (frequency response and kernel), across different bandwidths
- `filtparam-ncycles`: animation showing filter properties (frequency response and kernel), across different n_cycles
- `filtprop-burst-bandwidth`: animation showing the filter kernel, an input 'burst' signal, and output, across different bandwidths
- `filtprop-burst-ncycles`: animation showing the filter kernel, an input 'burst' signal, and output, across different n_cycles
