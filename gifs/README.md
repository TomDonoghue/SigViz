# Signal Visualizer Gifs

This folder is a collection of visualizers created for exploration signal processing.

Re-use is allowed, following the included license.

## Visualizers

Visualizers are organized into different topics.

Note that the numbered labeling of the folders here matches the numbered labeling under `notebooks`,
indicating where each visualizer is created.

### Timeseries

Timeseries visualizers include:
- `ts-osc`: time series, and associated power spectrum, of an oscillation
- `ts-white-noise`: time series, and associated power spectrum, of white noise
- `ts-pink-noise`: time series, and associated power spectrum, of pink noise
- `ts-brown-noise`: time series, and associated power spectrum, of brown noise
- `ts-comb`: time series, and associated power spectrum, of a combined signal, with an oscillation and pink noise
- `ts-comb-burst`: time series, and associated power spectrum, of a combined signal, with a bursty oscillation and pink noise

### Convolution

Convolution visualizers include:
- `convolution-short`: animated application of convolution, with a long kernel
- `convolution-long`: animated application of convolution, with a short kernel

### FFT

FFT visualizers include:
- `fft-aperiodic`: animated decomposition of the Fourier transform, applied to an aperiodic signal
- `fft-periodic`: animated decomposition of the Fourier transform, applied to a signal with a periodic component

### Models

Model visualizers include:
- `model-freq`: animated visualizer of a "frequency-by-frequency" feature set
- `model-band`: animated visualizer of a "band-by-band" feature set
- `model-peap`: animated visualizer of a "periodic-&-aperiodic" feature set
