a4MultiOpen documentation
=========================

.. toctree::
   :maxdepth: 2



a4MultiOpen
============

Bash script for loading of multiple a4db files.

Usage
-----

| a4MultiOpen [-a | -c | -s LIST_OF_FILES ]
| 
| Insert argument:
| 
| -a   opens all a3dbs in current directory.
|      Example: a4MultiOpen -a
| 
| -c   creates AnimatorMultiOpen session with only one file and immediately opens this file for further editing.
|      Example: a4MultiOpen -c
| 
| -s   creates AnimatorMultiOpen session with only a4dbs specified after -s argument.
|      Example: a4MultiOpen -s RR21_I_BBG_CSE135P32LW50_S01EG017.a4db RR21_I_BBG_CSE135P32LW50_S01EG016.a4db RR21_I_BBG_CSE135P32LW50_S01EG014.a4db


Description
-----------

This tool is used for fast opening of more than one a4db file.
Note: Please bear in mind, that single a4db uses approximately 5gb of RAM.



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
