.. toctree::
   :maxdepth: 2



Gap Evaluation
==============

Python script for META. Tested in META 20.1.1.

Computes gaps change, creates plots, annotations, images, spreadsheets and a presentation.

Replacement for old projects META_gaps_evaluation and pv1200.

Author: Ihor Mirzov, IDIADA.CZ. Please, do not hesitate to contact me via ihor.mirzov@idiada.cz for support.


Requirements
------------

* An opened model. The current state will be used for gap evaluation and have to contain the deformation results.

* Gap config file with gap descriptions for each opened model.

* Local coordinate systems assigned to each node of investigated gaps.

* Node sets named according to the appropriate gap.

* Sets of opposite nodeset named according to appropriate gap + _OP.

* All opened models should have the same gap groups and the same gap names.


Usage
-----

* Open one or two versions of the same bumper model. Use INP model to read geometry from - it contains information about local CSYSes created for all gaps.

* Select and activate needed States for each model. All node translations will be read from the selected states.

* Uncheck 'SYSTEMs' in 'View -> Visible Entities'.

* Run the script from the UserToolbars: *UserToolbars -> GapEvaluation*.

* Start working with the selecting of output folder for images, spreadsheets etc. Generated presentation will be saved here.

* Click on button 'Select config files for all models + process gaps' - a dialog will ask you for the Gaps Config Files for each opened model.

* Read log messages in the META Info window.

* Also you can format active window and save its screenshot clicking on corresponding buttons at any time.


Results
-------

For all opened models:

    1) For each gap group the script will generate:

    * A vector field for each gap group is created. It designates gap nodes translation direction and magnitude.

    * Frontal model view screenshot with marked Gaps belonging to the Group.

    2) For each gap group and for each local gap direction (normal/tangent) the script will generate:

    * Plots with gap curves: distance change between the nodes of the master and slave/opposite nodesets in local coordinate system vs. distance along gap. If there are two model versions opened at ones, each plot will contain curves for two models - for comparison reason. Curves for old model version are dotted, new curves are solid.

    * Spreadsheet with Min/Max node translations.

    * A text report with Min/Max node translations.

    * Annotations on model with Min/Max node translations.

    * Slide on the Report composer. As a template file *./bin/template.pptx* is used.


Gap config file
---------------

**DO NOT CHANGE COLUMN TITLES!**

Empty lines are skipped. To comment a line use symbols $ or #.

Each line represent one gap. Gaps a listed in a mirrored manner (see SYMM parameter).

**NAME** - name of the gap. Should correspond to the master nodeset name. Try to use a letter and a number - no words and special symbols. For example: A1 - for the left bumper side, A2 - for the right one. The script will search for node sets 'path_A1' and 'path_A2' or 'path_A1_NSET' and 'path_A2_NSET'. Those sets are treated as master sets. Opposite sets should have the same names + '_OP'.

**COLOR** - color name of the gap curves on plots. Could be one of: RED, GREEN, BLUE, CYAN, PURPLE, ORANGE, BLACK, GRAY.

**FIRST_NODE** - the number of the first node of the master node set.

**SYMM=1** - Curve x-values will be mirrored on the plot. **SYMM=0** - Usual x-values. Try to use SYMM=0 for the right bumper side, SYMM=1 - for the left one.

**NORMAL** - Name of local CSYS axis (with sign) for gap change evaluation in normal direction (default +z)

**TANGENT** - Name of local CSYS axis (with sign) for gap change evaluation in first tangent direction (default +y)

**TANGENT2** - Name of local CSYS axis (with sign) for gap change evaluation in second tangent direction (default +x)

**GROUP** - Name of the plot window to group curves in for the presentation. Gap curves, output images and vector fields are grouped together according to the GROUP name.

**Example gap config file:** ::

    $NAME      COLOR      FIRST_NODE    SYMM    GROUP    NORMAL    TANGENT    TANGENT2
    A1         RED        43090         0       Bumper   +z        +y
    B1         GREEN      195569        0       Lights   +z        +y
    C1         ORANGE     17575         0       Lights   +z        +y
    D1         BLUE       39091         0       Bumper   +z        +y
    $ ----------------------------------- symmetry -----------------------------------
    D2         BLUE       114926        1       Bumper   +z        +y
    C2         ORANGE     18129         1       Lights   +z        +y
    B2         GREEN      181933        1       Lights   +z        +y
    A2         RED        50616         1       Bumper   +z        +y

..
    For developers
    --------------

    toolbar.defaults contains User Form.

    +------------------+        +---------------------+
    |      BUTTON      +--------+   main.py: main()   |
    |      CLICK       |        |       models[]      |
    +------------------+        +----------+----------+
                                           |
    +------------------+        +----------+----------+
    |   gap.py: Gap    +--------+   model.py: Model   |
    |     curves[]     |        |        gaps[]       |
    +---------+--------+        +---------------------+
              |
    +---------+--------+        +---------------------+
    | curve.py: Curve  |        |      window.py      |
    |    direction     |        |      process.py     |
    |    minimum       |        |     settings.py     |
    |    maximum       |        |                     |
    +------------------+        +---------------------+


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
