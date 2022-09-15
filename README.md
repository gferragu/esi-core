# esi-core

Repository for compiled code used by ESI projects, namely C code used in the USGS Shakemap and Groundmotion-Processing programs.

As of September 15th, this project is functional for the gmprocess portion of compiled code. Shakemap functionality will soon follow.

## gmprocess

The compiled code here is used in [gmprocess](https://github.com/usgs/groundmotion-processing) both in metrics calculations and waveform processing.

Computation of waveform metrics utilizes the ```oscillators``` module, while waveform processing routines use the ```auto_fchp``` for corner frequency determination, as well as the ```konno-omachi``` and ```smoothing``` modules to perform spectral smoothing



## Shakemap

Under development for future PyPi release

Provides the [Shakemap](https://github.com/usgs/shakemap) project with necessary C libraries for Shakemap production and contouring
