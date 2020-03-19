bmwMatdbChecker documentation
=============================

.. toctree::
   :maxdepth: 2



bmwMatdbChecker
===============

Checks whether include contains obsolete BMW MatDB.

Usage
-----

bmwMatdbChecker [-u] [-l | INPUT_FILE]

Example
-------

| bmwMatdbChecker INPUT_FILE        # Checks given include
| bmwMatdbChecker -u INPUT_FILE     # Checks given include and updates matDB
| bmwMatdbChecker -l                # Checks latest modified include (.inc, .inp, .enc searched only)

Description
-----------

* Input file required, or parameter -l must be used
* Parameter -u causes run of BMW perl script
* Checks in .lis release notes files
* Support up to version v2.31
* Doesn't suppport parametric definition of materials, e.g. MATERIAL=<HARD_FOAM>
* ! perl script is modified, so the update files preserves name, and the original file gets .old.inc 



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
