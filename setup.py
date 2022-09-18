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

# contour_sourcefiles = ["src/shakemap/c/pcontour.pyx", "src/shakemap/c/contour.c"]

# clib_source = ["src/shakemap/c/clib.pyx"]

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
    # Extension(
    #     name="shakemap.c.pcontour",
    #     sources=contour_sourcefiles,
    #     libraries=["m"],
    #     include_dirs=[numpy.get_include()],
    #     extra_compile_args=[],
    # ),
    # Extension(
    #     name="shakemap.c.clib",
    #     sources=clib_source,
    #     libraries=["m", "omp"],
    #     include_dirs=[numpy.get_include()],
    #     extra_compile_args=["-Xpreprocessor", "-fopenmp"],
    #     extra_link_args=["-Xpreprocessor", "-fopenmp"],
    # ),
]

setup(
    ext_modules=cythonize(ext_modules),
)
