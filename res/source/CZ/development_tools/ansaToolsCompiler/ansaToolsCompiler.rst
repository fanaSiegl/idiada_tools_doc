.. toctree::
   :maxdepth: 2



AnsaToolsCompiler
=================

AnsaToolsCompiler is a script for compiling and exporting existing ansaTool (ANSA button) created by newPyProject script. ANSA native compiling method is used.

* copies given ansaTool to selected output directory
* updates internal imports (*.py -> *.pyb)
* compiles all located modules

Location
--------

ansaToolkit>ansaToolsCompiler

Usage
-----

* select main.py module of the tool to be compiled
* select output directory where the compiled version is going to be stored
* click ok

Requirements
------------

.. warning::
    
    All internal imports of non-standard modules must be done by ANSA native "ansa.ImportCode()" function!
    
* newPyProject-compatible script structure is required as input (to identify project name and directory structure properly)



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
