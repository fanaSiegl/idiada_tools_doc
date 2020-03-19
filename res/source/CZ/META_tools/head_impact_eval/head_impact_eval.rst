.. toctree::
   :maxdepth: 2



Evaulation of head impact
=========================

Python script for META - Evaulation of head impact

Usage
-----

Read the script in META 18.1.1 and newer.

Mata command:read ses /data/fem/+software/SKRIPTY/tools/python/metaTools/head_impact/main.py

Comment
------

Jan Stekly, 30.5.2017

For defined folder or working folder (default) find *DSY files inside of folder. For DSY files find corresponding *pc file. There are two options:
   - both files share the folder
   - or the model (based SKODA guidelines) is in subfolder MODEL. Folder MODEL(pc)/RESULTS(DSY/THP)
   
The script skip the folders which contain text "OLD" and "old".
 
   - The script read accelerations and evaluate g "3ms clip".
   - Save the picture and input it to report (Report/Report Composer) and finaly save preport with name head_impact.pptx.
   - Values of peaks it is possible to find in variables (Tools/Variables) and in the sheets (Report/Spreadsheets).
   - Acceleration is evaluated in node - varible "node".
   - The view of section is defined by 3 nodes - variable node1, node2, node3 (points of impaktor) and zoom (y coordination which defined zooming).
   - Each model/results have one page in the report.

Tomas Martinek, 5.11.2018
   - was add save the metadb
   - was added reading the second scalar - value of variable - scalar_name_append



Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
