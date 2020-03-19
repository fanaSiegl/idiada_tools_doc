
ABAQUS check GAP penetrations
======================================

Checks the penetration of GAP elements.

Compares relative node position (GAP: GA, GB) with the vector (GAP_PROP: C1, C2, C3)
and raises an error when Gap node position is incorrect.

Usage
-----

**Primary solver** - ABAQUS.

**Fix function** switches Gap node order (GA<==>GB).

