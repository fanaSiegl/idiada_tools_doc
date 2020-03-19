
PAMCRASH/ABAQUS check parts for Skoda
=====================================

Usage
-----

Check parts for the following rules:

* Number of segments = 5
* Delimiter for part name = __
* Number of digits for thickness = 1
* Max. number of chars = 80
* Contact thickness check = YES

  - the contact thickness should be same as thckness
  - some exceptions: contact thickness should be bigger than 0.5 and smaller then 3 mm

* Thickness by part name check = YES (not for Skoda)

**Primary solver** - ABAQUS/PAMCRASH.

**Fix function** is available for some warnings.

