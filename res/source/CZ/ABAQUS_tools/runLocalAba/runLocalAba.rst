AbaTools documentation
======================

.. toctree::
   :maxdepth: 2


runLocalAba
===========

Python script for running a local ABAQUS calculation.

* creates a new directory for calculation on scratch
* checks a free ABAQUS license and creates a correspondent configuration file
* runs ABAQUS calculation
* checks the calculation progress from *.sta file

Usage
------

runLocalAba [-h] inpFileName [Number of cores]

positional arguments:
  inpFileName      - Input *.inp file name.
  
  Number of cores  - Number of cores to be used for calculation.

optional arguments:
  -h, --help - show this help message and exit





