---
layout: default
---

# Overview

This website hosts a series of animated visualizers for exploring signal processing,
including demonstrating different kinds of time series and common processes in digital signal processing.

The code to make the animations, and copies of the visualizations are available in the
[source repository](https://github.com/TomDonoghue/SigViz).

## Table of Contents

This page contains the following sections:

- [Time Domain Signals](#time-domain-signals)
- [Fourier Transforms](#fourier-transforms)
- [Convolution](#convolution)
- [Filters](#filters)

### Time Domain Signals

The following plots show different kinds of simulated time series.

- the left plot shows the ongoing time series
- the right plot shows the corresponding power spectrum

#### Oscillatory Signals

First, we have an oscillatory signal, showing rhythmic activity:

![ts-osc](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-osc.gif)

#### Aperiodic Signals

Next, we will explore some aperiodic signals.

First, white noise, defined as having equal power across all frequencies (a flat power spectrum):

![ts-white](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-white-noise.gif)

<br>

Next, we have pink noise, which has a pattern of decreasing power
across increasing frequencies:

![ts-pink](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-pink-noise.gif)

<br>

Finally, we have brown noise, with has a steeper drop-off of power across increasing frequencies:

![ts-brown](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-brown-noise.gif)

<br>

#### Combined Signals

Next up, we have 'combined signals', which are a combination of periodic and aperiodic components:

![ts-comb](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-comb.gif)

Finally, we have a bursty signal:

![ts-comb-burst](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/01-timeseries/ts-comb-burst.gif)

### Fourier Transforms

In the following visualization, a time series (bottom left, black) is reconstructed (red), by a sum of many sinusoids (top left). On the right, the phase (top) and amplitude (bottom) of each sine wave is plotted.

#### Aperiodic Signal

In the following, the time series is an aperiodic, pink noise signal, decomposed by an FFT:

![fft-ap](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/02-fft/fft-aperiodic.gif)

Note that in the above, the signal is completely non-rhythmic.

Despite the signal not being rhythmic, it can still be
decomposed by a sum on sinusoids.

#### Periodic Signal

In the next signal, there is both an aperiodic component (pink noise), as well as
a periodic component (a 10 Hz rhythm).

![fft-pe](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/02-fft/fft-periodic.gif)

In the above signal, note how the prominent rhythm is fit by a sine wave which
stands out from the other frequencies, capturing the higher power in this frequency.

### Convolution

Here, a signal (grey) is convolved with a gaussian kernel (red), meaning we "slide" the kernel across the signal, computing each output value (green) by multiplying the kernel with the underlying signal (blue).

#### Long Kernel

In this first example, we will examine convolution using a long kernel.

![conv-long](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/03-convolution/convolution-long.gif)

#### Short Kernel

Next, we can examine how things are different when we use a shorter kernel.

![conv-short](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/03-convolution/convolution-short.gif)

#### Technical Notes

Some technical notes on the convolution:
- The "multiplication" applied between the kernel and the signal is the dot product
- Only the range where the kernel fully overlaps the signal is shown
- By definition, convolution applies the reverse of the kernel
    - In these examples, the kernel is symmetric, so it doesn't change anything

### Filters

This section explores applying (FIR) filters to time series.

#### Filters as Convolution

Applying a filter to a time series can be visualized as the convolution of a filter kernel with the data.

For a first example, we can see this as a filter kernel (for a narrowband bandpass filter) to a 'combined' signal:

![filtconv-combined](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtconv-combined.gif)

<br>

Notably, applying a filter does not guarantee the extraction of a rhythmic component of the signal.

For example, we can see this in the 'ringing' in the output of applying a filter to a step function:

![filtconv-step](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtconv-step.gif)

<br>

Notably, due to the shape of the filter kernel, outputs will tend to be smooth & rhythmic, even if the original data is neither.

For example, if we apply a bandpass filter to aperiodic (pink noise) data (non-rhythmic by definition) - the filter output still looks rhythmic:

![filtconv-aperiodic](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtconv-aperiodic.gif)

<br>

![filtconv-burst](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtconv-burst.gif)

#### TITLE

![filtout-step-ncycles](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtout-step-ncycles.gif)

![filtout-step-bandwidth](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtout-step-bandwidth.gif)

#### Filter Properties

![filtparam-ncycles](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtparam-ncycles.gif)

![filtparam-bandwidth](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtparam-bandwidth.gif)

#### TITLE

![filtprop-burst-ncycles](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtprop-burst-ncycles.gif)

![filtprop-burst-bandwidth](https://raw.githubusercontent.com/TomDonoghue/SigViz/main/gifs/04-filters/filtprop-burst-bandwidth.gif)
