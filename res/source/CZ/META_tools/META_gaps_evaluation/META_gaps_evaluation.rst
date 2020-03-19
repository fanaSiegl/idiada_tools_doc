.. toctree::
   :maxdepth: 2



META_gaps_evaluation
====================

Python script for META - computes gaps change, creates gap plots and annotations 

Usage
-----

Read the script in META 18.1.1 or newer
Or run it via UserToolbar

Description
-----------

The script computes gaps change, creates gap plots and annotations

Usage
-----

* Script can be run from the toolbar or from the script editor
* After launching of the script, the Open dialog will be occured requiring the SETUP file
* Pick the chosen setup file

Results
-------

* The script makes the curves for two directions - normal and tangent change of distance between the nodes
  (node belonging to the 'path' vs. node belonging to the 'path_OP') measured in local coordinate system
* Generate annotations on model/curves.

Requirements
------------

* Measure gap Setup file
* Local coordinate systems assigned to each node of investigated path
* Sets of nodes of given paths named according to appropriate paths
* Sets of opposite nodes of given paths named according to appropriate paths+_OP

Remarks
-------

.. warning::
    
    The cript suppose the user opened the model with all pre-requisites. The current state will be used for evaluation
    and have to contain the results - deformation.
    


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
