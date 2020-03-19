bmwPrepMassInp documentation
============================

.. toctree::
   :maxdepth: 2



BMW prepare masstrim inputdeck
===============================
Py3 script, that helps you with modifying inputdeck for masstrim with manual submit via flowguide or perl datacheck.
The script suggests inputdeck(s) to use, includes to comment and includes to add, however user is responsible for the correct selection from the currect directory files or list fo includes.
Therefore always check the files or list includes and do not trust the script.

* usage: bmwPrepMassInp [-h] [inputdecks [inputdecks ...]] 
    e.g. bmwPrepMassInp
    * the script will then guide you to select inputdeck(s), includes to comment, includes to insert.
    e.g. bmwPrepMassInp U06_H_VKBG_CSC2PP32R_H00EG029.inp U06_H_VKBG_CSC2PP32R_H00EG030.inp
    * the script will then guide you to select includes to comment, includes to insert.


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
