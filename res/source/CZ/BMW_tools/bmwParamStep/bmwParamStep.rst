bmwParamStep documentation
==========================

.. toctree::
   :maxdepth: 2



bmwParamStep
============

Python script for creating parametric ABAQUS STEP files for rear crash.
Creates:
* parameter files for each load case
* parametrized STEP files
* road positioning file

Usage
-----

| bmwParamStep -n             # Runs new configuration file wizard and creates the parameter files
| bmwParamStep -f FILE_NAME   # Creates the parameter files based on the configuration file provided by the user


| If "-n" was chosen (you don't have config file):
|
| 1) Read questions and write answers + Return (don't worry if you accidentally put some wrong value - it can be modified afterwards)
| 2) After that the config file (suffix *.conf) and all necessary files are created 

Notes
-----

* You can modify config, but watch out. Do not modify the strange config syntax. Only values!

* | If you want to modify config, then modify the variant number inside (safe side - because config can overwrite old files if is the naming overlapping) 
  | 
  | # The variant number (for example 01v001)
  | our $varnum ='01v001';
  | 
  | to 
  | 
  | # The variant number (for example 01v001)
  | our $varnum ='01v001a';



Description
-----------

It is necessary to have:

* Front/Heck datacheck opened in animator for dimensions of the car
* Task description for MASS and ASO/WHA
* Wheels for dimensions (for example 205x55xR16)
* Input file (check if sets for CLOAD exist)
* | Sets according to MOKA:
  | S61199011;AAA_AufhVA_CLOAD_3270_vo_li
  | S61199013;AAA_AufhVA_CLOAD_3271_vo_re
  | S61699011;AAA_AufhHA_CLOAD_4210_hi_li
  | S61699013;AAA_AufhHA_CLOAD_4211_hi_re
  |
  | If they aren't in input, then you choose "0" while the "script" is running.
  | The script creates these sets and fill it with nodes on wheels (you will be asked for these nodes)



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
