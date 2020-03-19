dagDynaQueue documentation
==========================

.. toctree::
   :maxdepth: 2



dagDynaQueue
============

Script for starting LS-Dyna on German local machines.

Usage
-----

| dagDynaQueue INPUTDECK [-n NUMBER_OF_CPUS] [-p PRIORITY] [-d] [-skip FILE_LIST]
| dagDynaQueue INPUTDECK [--ncpu NUMBER_OF_CPUS] [--priority PRIORITY] [--datacheck] [-skip FILE_LIST]
| dagDynaQueue -c CALCULATION_FOLDER [-n NUMBER_OF_CPUS] [-p PRIORITY] [-d]
| dagDynaQueue -x

Description
-----------

* Prerequisities:
    * access to German network
    * running cron.sh script on all German machines, which are to be used for calculation 
    * working rundyna.sh script on German directories 
    * .qdyna.env file copied into home directory (examples may be downloaded by dagDynaQueue -x, remove suffix .cz or .muc afterwards)
* Function:
    * Creates calculation directory in current folder and synchronizes data into the folder defined in .qdyna.env file
    * Runs simulation in LS-Dyna R 9.3.0 in single precision, with dedicated memory 400 MB
    * Saves LOG info in directory defined in .qdyna.env file
* Options:
    * -n | --ncpu:          Number of CPUs used; do not use more than 6; default=5
    * -p | --priority:      Lower value means higher priority; default=2
    * -d | --datacheck:     Simulation is run with "mcheck=1" flag, i.e. in model check mode
    * -x | --example_env:   Downloads example environment files      
    * -c | --calcdir:       Provides calculation directory   
    * -h | --help:          Displays this help
    * -s | --sync_results:  Syncs all available results from German scratch to CZ
    * -skip:                Skip copying of the provided files


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
