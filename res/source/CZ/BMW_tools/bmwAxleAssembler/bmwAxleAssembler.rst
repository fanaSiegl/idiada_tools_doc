bmwAxleAssembler documentation
==============================

.. toctree::
   :maxdepth: 2



BMW Axle Assembler
===============================
Python3 script, that assembles or disassemles axle (HA, VA) includes.

* usage: bmwAxleAssembler [-h] [-a] [-d] [subfiles [subfiles ...]]
* Works in two modes: Assemble, Disassemble

* -a for assemble mode:
    * assembles all files given after the argument "-a" into "axleMerged.inc" submodel:
    bmwAxleAssembler -a axleHeader.inc axleSub01.inc axleSub02.inc axleSub03.inc axleStep.inc
    
    * if no files are given, the script automatically searches for "axle*.inc" patterns:
    bmwAxleAssembler -a

* -d for disassemble mode:
    * disassembles submodel given after the argument "-d" into "axle*.inc" submodels:
    bmwAxleAssembler -d IX_VBBG_HA_DYN-HAT-2846178_GFZ01v005.inc


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
