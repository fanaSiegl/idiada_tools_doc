odbZip documentation
====================

.. toctree::
   :maxdepth: 2

odbZip
======

Python script for ".odb" file archiving and additional ABAQUS analysis clean up.

* searches in current directory and all sub-directories for *.odb files and creates a *.zip archive.
* creates a "removeFiles.script" file containing file paths of specified extensions (*.msg, *.com, *.prt, *.sim, *.sta, *.odb, *.stt, *.sel, *.res, *.pac)
* by executing this "removeFiles.script" file all files will be deleted

Usage
-----

odbZip

