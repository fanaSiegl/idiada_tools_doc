.. toctree::
   :maxdepth: 2



Impactor Position
=================

The script for a set of given geometrical points rotates and translates the impactor.

Separate model and position files for each point are generated.


Location
--------

From ANSA menu click:

Tools > Scripts > User Script Buttons:

Tools > ImpactorPosition


Usage
-----

- Open MODELNAME_XXX_VERSION in ANSA.

- Click on User Script Button 'Tools > ImpactorPosition' or...

- ...Load Python source file into ANSA Script Manager - the scipt will run automatically.

Deck could be ABAQUS or PAMCRASH. Default is ABAQUS.
If it's needed, user may set PAMCRASH manually.
It affects generated files format: .inp or .pc.
Include files will always have extension .inc.
Position file format strongly depends on chosen deck.

Model's name should be something like:
'TOYOTA_G3_B_RBU_RIGIDITY_XXX_001-03.inp'.
This name is interpreted as MODELNAME_XXX_VERSION.extension.
Extension could be 'ansa', 'inp' or 'pc'. There must be two
template files in model's (working) directory:
MODELNAME_XXX_VERSION.inp (or .pc) and MODELNAME_position_XXX.inc.
Template files should have accurate headers.
For each geometrical point _XXX_ in template names and
template headers will be replaced with point's name.

It is supposed that:

- impactor's bottom face's center coinsides with global CSYS origin,

- impactor's normal coincides with global Z-axis.

Projection tolerance is 100 mm and is fixed!


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
