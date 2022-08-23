# esi-core

Repository for compiled code used by ESI projects. 

## Introduction

This is a utility library of compilied code for gmprocess and ShakeMap. The code
here represents the innermost loops that need to be very high-performance. We will
add more code and documentation as time passes, but right now this is code ripped
from the two repos.

You will almost never use this library on its own. It is intended to be incorporated
into other environments, namely gmprocess and ShakeMap.

See tests directory for usage examples.

## Installation

From repository base, run
```
conda create --name esi_core pip
conda activate esi_core
pip install .
```

## Tests

```
pip install pytest
pytest .
```
