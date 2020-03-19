.. toctree::
   :maxdepth: 2



dynTransformCreator
==============

Based on a pair of three points coordinates, creates a code for LS-Dyna transformation of include or nodes

Usage
-----

| dynTransformCreator <INPUT PARAMETER FILE> [-t <TITLE>] [-id <Transformation ID>] [-i <Include name> | -n <Node set Id>] 
|
| default     creates trasnformation with Id 10000 without title
| -t          applies title to *DEFINE_TRANSFORMATION keyword 
| -id         defines Id of transformation
| -i          creates *INCLUDE_TRANSFORM keyword with path to the include
| -n          creates *NODE_TRANSFORM keyword with ID of set of nodes to be transformed

Examples
--------

| dynTransformCreator example_file
| dynTransformCreator example_file -t Airbag transformation
| dynTransformCreator example_file -t Airbag transformation -id 6001001
| dynTransformCreator example_file -t Airbag transformation -id 6001001 -i airbag_model.key
| dynTransformCreator example_file -t Airbag transformation -id 6001001 -n 66001

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
