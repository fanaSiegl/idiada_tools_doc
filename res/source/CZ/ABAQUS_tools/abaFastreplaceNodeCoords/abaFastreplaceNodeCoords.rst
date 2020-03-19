abaFastreplaceNodeCoords documentation
======================================

.. toctree::
   :maxdepth: 2



abaFastreplaceNodeCoords
========================

A fast ABAQUS node replacer written in C++

Usage
-----

abaFastreplaceNodeCoords [-f] IMAGE_FILE TARGET_FILE OUTFILE

-f  parameterized coordinates are replaced as well

Description
-----------

Replaces nodes coordinates in TARGET_FILE by coordinates defined in IMAGE_FILE

Notes
-----

* Node definition lines consist of an ID and three coordinate values, separated by commas. We do check that ID is an integer, but we do not check that the coordinates in IMAGE_FILE are valid numbers.
* If the same node is defined more than once in IMAGE_FILE, the additional definitions are ignored.
* Trailing whitespaces and carriage returns are not copied.
* By default, node coordinates in TARGET_FILE are replaced only if they are given by explicit numbers. 



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
