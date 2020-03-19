abaNMAPCreator documentation
============================

.. toctree::
   :maxdepth: 2



abaNMAPCreator
==============

Based on a pair of three points coordinates, creates a code for NMAP or block of parameters usable in *SYSTEM.

Usage
-----

| abaNMAPCreator <INPUT PARAMETER FILE> [-n] [-p <Parameter prefix name>] [-s <NMAP set name>] 
| 
| default     creates 1 NMAP to define trasnformation
| -n          creates 3 NMAPs for rotations and 1 for translation
| -p          prints block of PARAMETERs for SYSTEM definition
| -pp         prints block of PARAMETERs with a prefix for parameter default names
| -s          defines name of a set, on which the NMAP is applied

Examples
--------

| abaNMAPCreator example_file
| abaNMAPCreator example_file -n
| abaNMAPCreator example_file -n -s 'S999999;SAB_Front'
| abaNMAPCreator example_file -p
| abaNMAPCreator example_file -pp 'Batterie_G491111_'

Description
-----------

* Based on script 'moveseat' by Rainer Moll, IDIADA FZT <rainer.moll@idiada.com>
* Performs a rigid body transformation determined by three points, using Kabsch algorithm:
    P_i --> Q_i (i=1,2,3)
* References
    http://math.stackexchange.com/questions/222113/given-3-points-of-a-rigid-body-in-space-how-do-i-find-the-corresponding-orienta


Input parameter example
-----------------------

# source coordinates
1245.42,    -194.116,   -21.9871
1632.59,    -621.016,   -69.5177
1243.81,    -615.65,    -21.7861
# target coordinates
1247.87,    -199.114,   13.8104
1636.46,    -626.015,   -20.1793
1246.25,    -620.648,   13.9551

The numbers may be separated by whitespace and/or commas.
Number of coordinates must be three. 


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
