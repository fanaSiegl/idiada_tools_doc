abqMerge documentation
======================

.. toctree::
   :maxdepth: 2



Abaqus Keyword Blocks Merger
===============================
Python3 script, that merges chosen keyword blocks between two abaqus includes.

* takes selected entities (nodes, elements, pids[=sections], sets [and surfaces]) from "from_file"
* takes rest of the entities from "to_file"
* merges them into new "out_file"

* usage: abqKeywordBlocksMerger [-h] [-n] [-e] [-p] [-s] -f sub_v001a.inc -t sub_v001.inc [-o sub_v002.inc]

* required arguments:
    * -f/--from sub_v001a.inc,
    * -t/--to sub_v001.inc,

* optional arguments:
    * -h/--help
    * -n/--nodes,
    * -e/--elements,
    * -p/--pids,
    * -s/--sets and surfaces,
    * -o/--out sub_v002.inc,


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
