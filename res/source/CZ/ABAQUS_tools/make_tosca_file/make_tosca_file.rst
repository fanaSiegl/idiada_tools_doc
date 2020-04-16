.. toctree::
   :maxdepth: 2



Tosca - making the par file from ABAQUS file
============================================

Motivation
----------
- make the par file definition for TOSCA based on the inp file with the step/cload definition
- simplify the process of par file definition

Description
-----------
* from inp are extracted the STEPS/LOADCASES based the order
   - for the entities are generated the COMPLIANCE responses separately
   - it is possible to for each COMPLIANCE define weight factor
       + *file: Include_objective_func_compliance_MIN.par*
* for each STEPS/LOADCASES the CLOAD points are defined the responses and constrains 
   - for each node of CLOAD is defined the Tosca GROUP
      + *the file: Include_groups.par*
   - for each STEP/LOADCASE is defined the response at Tosca GROUP (for Abaqus CLOAD)
   - the constrains is not applied to optimization setting
      + *the file: Include_response_disp_constrain_1_mm.par*
   - the constrains - the displacements at CLOAD points are not applied 
     to optimization setting
* for each CLOAD points are defined the Tosca variables
   - the variables are desined only for better way of checking the responses (displacements)
   - the variables are defined for STEP/LOADCASE and CLOAD nodes
      + *the file: Include_topology_setting.par*
* the rest of setting is fixed:
   - the group of design space (necessery to updated the properties name)
      + *file: Include_groups.par*
   - the design space is define
      + *file: Include_design_variable.par*
   - the response constrain to volume - reduction to 30% of origin design space
      + *file: Include_response_vol_constrain_0_3.par*
   - design constrain - manufacture constrian (for injection - CAST) - need to be defined a vector
      + *file: Include_topology_design_constrain_volume_MANUFACTURE.par*
   - design constrain - max member
      + *file: Include_topology_design_constrain_volume_MAX_MEM_8.par*
* all par includes are included to: TP_optimization_MIN-compliance_constrain-vol_30_001.par 
   

Comments
--------

* the includes in inp file are supported
* the STEPs and LOADCASEs are supported
* usually is necessery modify additional technology constrains e.g. symmetry "TP_LINK", ...
* some parameters should be manualy modified..
    


Usage
-----


usage::


    abaqus2tosca input_file.inp


example::


    abaqus2tosca S214.inp


Revision history
----------------

Application revision history overview.

.. toctree::
   :maxdepth: 2

   revision_history.rst
