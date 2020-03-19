bmwTicketCalculator documentation
=================================

.. toctree::
   :maxdepth: 2



bmwTicketCalculator
===================

Tool for generating eBAS tickets from worked hours.

Usage
-----

| bmwTicketCalculator WORKED HOURS[h] [-c COST] [-p PROJECT] [-i TICKETS_TO_IGNORE]  
| bmwTicketCalculator MONEY_VALUE [-p PROJECT] [-i TICKETS_TO_IGNORE] 
| bmwTicketCalculator MONEY_VALUE [-p PROJECT] [-u TICKETS_TO_USE] 
| bmwTicketCalculator MONEY_VALUE [--project PROJECT] [-\-cost COST] [-\-ignore TICKETS_TO_IGNORE] 
| bmwTicketCalculator MONEY_VALUE [--project PROJECT] [--use TICKETS_TO_USE] 

Example
--------

| bmwTicketCalculator 62.5h
| bmwTicketCalculator 1480.1
| bmwTicketCalculator 62.5h -c 35 -p side 
| bmwTicketCalculator 62.5h -i INT CAD
| bmwTicketCalculator 62.5h -u ANA EVA ASH


Description
-----------

* Input:
    * in hours:         use NUMBER[h], e.g. 156.2h
    * in euros:         use NUMBER, e.g. 1481.6
    * Both dot and comma are supported as decimal separators 
* Options:
    * -p | --project    Project: heck, side, front;     default = heck
    * -c | --cost       Cost of manhour;                default = 33 EUR
    * -i | --ignore     Ignore list of tickets;         default = None
    * -u | --use        use only defined tickets;       default = CAD, ANA, MESH, ASH, ASS, ASF, VAR, EVA, INT
    * Note: Use of ASH, ASS or ASF tickets is always determined by project and overrides tickets provided in --use option
    * Either parameter --use or --ignore can be used, not both


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
