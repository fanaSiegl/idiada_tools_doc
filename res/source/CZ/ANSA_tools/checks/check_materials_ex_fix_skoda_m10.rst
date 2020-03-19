
PAMCRASH check materials for Skoda
==================================

Check materials based matching list and name in properties name.

Usage
-----

**Primary solver** - ABAQUS/PAMCRASH/NASTRAN.

**User defined parameters**:

- delimiter for part name of segment e.g. __
- number of segments of names of properties e.g. 5
- type of loadcase e.g. COMMON 
  in case of empty parametr, the list of loadcases is popup
  in case of only one loadcase in matching list is appied just this
- segment of material name e.g. 5
- matching list - /data/fem/+software/SKODA_INCLUDE/white_list

**Fix function** is available for some warnings.

