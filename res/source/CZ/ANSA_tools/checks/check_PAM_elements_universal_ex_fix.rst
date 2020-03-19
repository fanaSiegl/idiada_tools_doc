
Check elements 
====================

Check the shell and solid elements.

Usage
-----

**Primary solver** - ABAQUS/PAMCRASH/LSDYNA
**Car maker** - SKODA, AUDI and DAYMLER

* The ANSA quality file is choosed based:
   -  The use can choose own User quality mesh file
   -  Default mesh length value: 5 and Material type (polymer/steel): polymer (only for Skoda and Daimler and for setting above is predefined an ANSA quality file)
   -  In case that user dont fill User quality mesh file and parameters from above are different then default then will be uses the current F11 quality parameters
* Basic check of elements is realized xxx.ansa_qual file
* Special rules are applied for SKODA:
   -  User defined check element: min_lenght = THICKNESS FACTOR * thickness
   -  User defined check element for skew: TRIA = 60.0, QUAD = 48.0
* Special rules are applied for DAIMLER:
   - check MIN HEI only for TETRA
* Possible compress list bigger then e.g. 100 lines

