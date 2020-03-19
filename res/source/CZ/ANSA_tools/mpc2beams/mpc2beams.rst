rbe2beams documentation
=======================

.. toctree::
   :maxdepth: 2




mpc2beams
=========

Tool for a conversion of ABAQUS MPC entities to BEAM entities respecting connected materials. If elements with xx_CONNECTION_xx property are connected to mpc, this element property is unified according surrounding mesh property.

Usage
-----

click button and select MPC enetities to be converted.

Description
-----------

* according to selected MPCs locates connected shell elements
* unifies the xx_CONNECTION_xx property
* creates BEAM elements



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history
