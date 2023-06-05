# -*- coding: utf-8 -*-

import os
import numpy

from setuptools import Extension, setup
from Cython.Build import cythonize

osc_sourcefiles = [
    "src/esi_core/gmprocess/metrics/oscillators.pyx",
    "src/esi_core/gmprocess/metrics/cfuncs.c",
]
ko_sourcefiles = [
    "src/esi_core/gmprocess/waveform_processing/smoothing/konno_ohmachi.pyx",
    "src/esi_core/gmprocess/waveform_processing/smoothing/smoothing.c",
]
auto_fchp_sourcefiles = ["src/esi_core/gmprocess/waveform_processing/auto_fchp.pyx"]

contour_sourcefiles = [
    "src/esi_core/shakemap/pcontour.pyx",
    "src/esi_core/shakemap/contour.c",
]

geo_source = ["src/esi_core/shakemap/geodetic_distances.pyx"]
cov_source = ["src/esi_core/shakemap/covariance_matrix.pyx"]

libraries = []
if os.name == "posix":
    libraries.append("m")

ext_modules = [
    Extension(
        name="esi_core.gmprocess.metrics.oscillators",
        sources=osc_sourcefiles,
        libraries=libraries,
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-O1"],
    ),
    Extension(
        name="esi_core.gmprocess.waveform_processing.smoothing.konno_ohmachi",
        sources=ko_sourcefiles,
        libraries=libraries,
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-O2"],
    ),
    Extension(
        name="esi_core.gmprocess.waveform_processing.auto_fchp",
        sources=auto_fchp_sourcefiles,
        libraries=libraries,
        include_dirs=[numpy.get_include()],
        extra_compile_args=["-O2"],
    ),
    Extension(
        name="esi_core.shakemap.pcontour",
        sources=contour_sourcefiles,
        include_dirs=[numpy.get_include()],
        extra_compile_args=[],
    ),
    Extension(
        name="esi_core.shakemap.covariance_matrix",
        sources=cov_source,
        include_dirs=[numpy.get_include()],
    ),
    Extension(
        name="esi_core.shakemap.geodetic_distances",
        sources=geo_source,
        include_dirs=[numpy.get_include()],
    ),
]

setup(
    ext_modules=cythonize(ext_modules),
)
