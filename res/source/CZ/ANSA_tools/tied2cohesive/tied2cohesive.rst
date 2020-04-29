.. toctree::
   :maxdepth: 2



Tied to COHESIVE elements
=========================

The script convert the tieds to cohesive elements.

* is applied only for visible tieds !
* convert the slave elements to connection face
* based the connection face is generated the cohesive elements
* the cohesive elements are pasted to slave elements of origin tied
* the origin tied is modified - the slave nodes are now the cohesive nodes
  close to mater group of tied
* the common setting was applied - it is possible to modify inside of 
  script body

Location
-------- 
User Script buttons - Tools>tieds2cohesive

Usage
-----

* show the tieds which you want to convert to cohesive
* click the button 
* check the elements
* check the origin tieds

Requirements
------------

* designed for ANSA 20.1.1
* works also for ANSA 19.1.1


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
