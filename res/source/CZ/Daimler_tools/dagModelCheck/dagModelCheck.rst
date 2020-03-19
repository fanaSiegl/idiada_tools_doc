dagModelCheck documentation
===========================

.. toctree::
   :maxdepth: 2



dagModelCheck
============

Python script to create simple model check simulation and send to queue.

Usage
-----

| dagModelCheck -i INCLUDE -b BOUNDARY_CONDITIONS [-n]
| dagModelCheck -x     

Description
-----------

* Creates a simulation from inputdeck template and provided includes, 40g-pulse in Y direction    
* Requires: 
    * -i | --include :              include to be checked 
    * -b | --boundary :             include with *SET_NODE (Id 60001) containing nodes, to which boundary conditions are applied
* Options:
    * -x | --download_example :     example include files are downloaded
    * -n | --dry_run :              the simulation is prepared, but not sent to the solver (nor German network)    


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
