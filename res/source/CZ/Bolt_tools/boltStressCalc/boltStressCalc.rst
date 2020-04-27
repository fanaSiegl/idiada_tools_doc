.. toctree::
   :maxdepth: 2



Screws stress evaluation
============

Project function description.

* Requires file Inputs.txt to be read as an argument and .dat file from abaqus to be processed.
  
* Uses file screwTables.txt containing selected metric screws dimensions and file strengthClasses.txt containing values of maximum allowable stress in bolts. Both files are located in /res folder in script directory. 

* Calculates maximum equivalent stress in bolt by comparing equivalent stresses in all beams inside specified ELSET. The equivalent stress includes contributions from tightening torque and working loads. Tightening torque is computed based on norm VDI 2230 (it uses user specified pretension force, friction factors and consideres friction in thread and under the nut). The equivalent stress in the bolt is than compared to maximum allowable stress which is min(Rp02/S1,Rm/S2). Utilization factor (which is 1/safety_factor) is computed.

* Outputs txt file summarizing the outputs for specified elset of given dat file at specified time.


Usage
-----

usage::

    boltStressCalc [input parameter]

example::

    boltStressCalc "Inputs.txt"

Remarks
-------

.. warning::
    
    Requires input text file
    
* requires input text file
* calculates stress in bolt resulting from application of tightening torque and work load
* creates output text file



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
