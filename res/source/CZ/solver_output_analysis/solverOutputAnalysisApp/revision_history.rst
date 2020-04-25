
Revision history
================

Revision history graph::
    
       * commit e9bd27f (HEAD, tag: V.0.3.3, origin/master, origin/HEAD, master)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Sat Apr 25 18:30:50 2020 +0200
   | 
   |     information tab - mouse action tuning
   |  
   * commit 94d2273 (tag: V.0.3.2)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Apr 24 18:19:47 2020 +0200
   | 
   |     fixed popup messages in meta
   |  
   * commit 7cd0dff
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Apr 24 18:05:05 2020 +0200
   | 
   |     added context menu on RMB in ListViews
   |  
   * commit 8a650d2 (tag: V.0.3.1)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Feb 17 09:14:15 2020 +0100
   | 
   |     LINE #650 in abaqusio, BLOCK_END = '.' to the AbaqusContLogBlock class
   |     Also added try/except to abaqusio to standalone testing
   |  
   * commit a8f1224 (tag: V.0.3.0)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Jan 31 09:08:53 2020 +0100
   | 
   |     Fixed highlight text
   |     added licensing
   |     added contact set coloring in ansa and meta
   |     added recursion option to open global contact entity card to fix sets defined by range
   |  
   * commit d61ff96
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jan 27 13:39:57 2020 +0100
   | 
   |     Import manual merge :(
   |    
   *   commit 933dd4b
   |\  Merge: 3943f54 3c5fdab
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Mon Jan 27 13:23:57 2020 +0100
   | | 
   | |     Merge branch 'beta_import'
   | |   
   | * commit 3c5fdab
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Mon Jan 27 13:19:18 2020 +0100
   | | 
   | |     Dummy commit
   | |   
   * | commit 3943f54
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Mon Jan 27 13:23:39 2020 +0100
   | | 
   | |     Revert "Revert "Revert "Merge /data/fem/users/siegl/eclipse/solverOutputAnalysisApp"""
   | |     
   | |     This reverts commit 67c3812e5c9e3348623def78d9175d4b90854e65.
   | |   
   * | commit 67c3812
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Mon Jan 27 13:22:07 2020 +0100
   | | 
   | |     Revert "Revert "Merge /data/fem/users/siegl/eclipse/solverOutputAnalysisApp""
   | |     
   | |     This reverts commit 421b06ea3dad6d203b3aa69ad36e79389ad32112.
   | |   
   * | commit 421b06e
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Mon Jan 27 13:09:21 2020 +0100
   | | 
   | |     Revert "Merge /data/fem/users/siegl/eclipse/solverOutputAnalysisApp"
   | |     
   | |     This reverts commit 4b1a4f18d799905fb509b34a7ef53ea0d2072f9a, reversing
   | |     changes made to ff23fd5af340f7840cbb499c642165efefb6f192.
   | |     
   * |   commit 4b1a4f1
   |\ \  Merge: ff23fd5 4abac64
   | |/  Author: Milos Cadek <milos.cadek@idiada.cz>
   | |   Date:   Mon Jan 27 13:02:04 2020 +0100
   | |   
   | |       Merge /data/fem/users/siegl/eclipse/solverOutputAnalysisApp
   | |       
   | |       Conflicts:
   | |       	bin/interfaces/abaqusio_bash.py
   | |   
   | * commit 4abac64
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Thu Jan 16 14:09:14 2020 +0100
   | | 
   | |     ansa/meta import compatibility implemented. Required for further script compiling!
   | |   
   | * commit 67d6d46
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Tue Jan 14 15:59:05 2020 +0100
   | | 
   | |     Windows compatibity of domain/abaqusio_bash implemented. Bash "grep" command replaced by cmd "findstr".
   | |   
   * | commit ff23fd5 (tag: V.0.2.9)
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Mon Jan 27 10:49:19 2020 +0100
   | | 
   | |     fixed initial penetrations in heuristics
   | |     - added a file path to main window title
   | |   
   * | commit 1add82b (tag: V.0.2.8)
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Tue Jan 21 14:41:58 2020 +0100
   | | 
   | |     placement atribute in abaqusio bug
   | |   
   * | commit dd2abf1
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Tue Jan 21 14:39:17 2020 +0100
   | | 
   | |     bug fixed - abaqusio - placement - AbaqusInitStatus
   | |   
   * | commit 5e4e820 (tag: V.0.2.7)
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Tue Jan 21 12:09:40 2020 +0100
   | | 
   | |     menu label rename
   | |   
   * | commit ba5fa3c
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Tue Jan 21 10:40:43 2020 +0100
   | | 
   | |     Minor changes
   | |   
   * | commit 1fbaef6 (tag: V.0.2.6)
   |/  Author: Milos Cadek <milos.cadek@idiada.cz>
   |   Date:   Thu Jan 16 14:47:55 2020 +0100
   |   
   |       - added windows support
   |       - ansa UI update
   |  
   * commit 62490c2 (tag: V.0.2.5)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Jan 13 17:18:17 2020 +0100
   | 
   |     ansa minor fix of identify buttons
   |  
   * commit c2e4974 (tag: V.0.2.4)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Jan 13 17:07:05 2020 +0100
   | 
   |     ansa update
   |  
   * commit 859285d (tag: V.0.2.3)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Jan 13 09:56:59 2020 +0100
   | 
   |     Fixed items:
   |     U/C in status files
   |     initial penetrations werent disp. correctly
   |     numbering of warnings and errors in heur.
   |     slight improvement in performance - added break statements in parser
   |     fixed view reduction in msg files
   |     added buttons in convergence/status tabs
   |  
   * commit 4161d70 (tag: V.0.2.2)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Nov 21 09:21:23 2019 +0100
   | 
   |     minor fix
   |     - convergence check statement changed to 'FORCE    EQUILIB. ACCEPTED'
   |     because its more general and shorter
   |  
   * commit 75e31b0 (tag: V.0.2.1)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Nov 21 08:20:36 2019 +0100
   | 
   |     Minor fix in status file view - convergence coloring
   |     - added 'C' in status file when convergence blocks are missing
   |  
   * commit bf7fc58 (tag: V.0.2.0)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Nov 14 15:45:08 2019 +0100
   | 
   |     major change in heur
   |     
   |     -status file label change
   |     -fix in abaqusio when reading residual value as (251.)
   |     -created sub-containers for heur items, added PARENT_NAME attribute
   |     - Beam set error item moved from heur to pre
   |  
   * commit 1a239f7 (tag: V.0.1.10)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Nov 4 08:48:02 2019 +0100
   | 
   |     META app complete update
   |     
   |     + added several heur items
   |  
   * commit 0d9a7f8 (tag: V.0.1.9)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 31 16:31:46 2019 +0100
   | 
   |     Bugs fixed in heuristic logs - ANSA
   |     
   |     - heur items have now a placement information (step, inc, att)
   |     - heur items were displayed wrongly, there was an error in assigning them to
   |     certain increment, since blockId was given by cumulative block count
   |     which wasnt taking in account the fact that 1 inc can be run multiple times,
   |     with several attempts
   |     
   |     NOTE: META version was not fixed with this release
   |  
   * commit 0658a29 (tag: V.0.1.8)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 29 16:07:49 2019 +0100
   | 
   |     Minor bugs fixed.
   |     
   |     - MPC/FASTENER/CONNECTOR not disp. properly on LMB on entity
   |     - in heur 'all' moved to first place
   |     - in heur added explanations to heur items / within * - *
   |  
   * commit ca1820b
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 24 17:29:53 2019 +0200
   | 
   |     performance boost - bash power
   |     
   |     - redefined dat file reading
   |     - using bash and grep command with subprocess lib
   |  
   * commit bf489f0
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 22 08:01:09 2019 +0200
   | 
   |     Gap/Con elem show only added
   |  
   * commit fc72058
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Oct 21 16:00:18 2019 +0200
   | 
   |     Added new window Sets/Contacts
   |     
   |     - replaced checkboxes for mouse action control with comboboxes
   |     - fixed cont log block end pattern
   |     - added mouse action controls for Sets/Contacts
   |  
   * commit c1edaf2 (tag: V.0.1.7)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 15 16:20:35 2019 +0200
   | 
   |     LMB, RMB behav hotfix 2
   |     
   |     added new filters for msg file view
   |     fixed move cursor/highlight behav
   |  
   * commit 8d167f4 (tag: V.0.1.6)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 15 11:12:50 2019 +0200
   | 
   |     ansai showOnlyPartFromNode - IndexError exception added
   |  
   * commit 531a61b (tag: V.0.1.5)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 15 10:08:00 2019 +0200
   | 
   |     LMB, RMB behav fixed
   |  
   * commit 281a64a
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Oct 15 09:44:49 2019 +0200
   | 
   |     Added PopUpMenu class in ansai, metai
   |     - reducing msg file viewed text
   |     
   |     Bugs fixed:
   |     LMB click action on covergence log list view:
   |     Traceback (most recent call last):
   |       File "/data/fem/+software/SKRIPTY/tools/python/solverOutputAnalysisApp/default/bin/presentation/ansa_base_widgets.py", line 390, in _onMouseClickFunction
   |         infoWidgetItem = guitk.BCListViewItemGetUserData(item)
   |     RMB click action on convergence log list view:
   |     - show only PID wasnt working in all cases
   |  
   * commit f711a82
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Oct 11 16:16:53 2019 +0200
   | 
   |     Created new block:
   |     AbaqusIncInitContStatusChange - special blocks
   |     r.content['STEP'][0].content['INCREMENT'][2].content['ATTEMPT'][0].specialContent['INIT']
   |     - detects cont status change between increments - outside convergence blocks
   |     NOTE:
   |     r.specialContent['INIT'] -- is collecting initial penetrations (contact status)
   |     
   |     Added msg file view reduction in META
   |     Redefined delete function for base block instances (adding weak reference)
   |     In abaqus_items:
   |     - new function for msg file view reduction
   |     _reduceTxtBlockInitContLog, _reduceTxtBlockGapLog, _reduceTxtBlockContLog, _reduceTxtBlockInitContLog
   |     
   |     Fixed:
   |     - crash when clickin in heuristic tab on navigation (sta file)
   |     - list view is now not showing empty - None items (ie. when Moment information is missing in convergence block)
   |  
   * commit 7bf3a34
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Oct 11 16:08:19 2019 +0200
   | 
   |     Created new block:
   |     AbaqusIncInitContStatusChange - special blocks
   |     r.content['STEP'][0].content['INCREMENT'][2].content['ATTEMPT'][0].specialContent['INIT']
   |     - detects cont status change between increments - outside convergence blocks
   |     NOTE:
   |     r.specialContent['INIT'] -- is collecting initial penetrations (contact status)
   |     
   |     Added msg file view reduction in META
   |     Redefined delete function for base block instances (adding weak reference)
   |     In abaqus_items:
   |     - new function for msg file view reduction
   |     _reduceTxtBlockInitContLog, _reduceTxtBlockGapLog, _reduceTxtBlockContLog, _reduceTxtBlockInitContLog
   |     
   |     Fixed:
   |     - crash when clickin in heuristic tab on navigation (sta file)
   |     - list view is now not showing empty - None items (ie. when Moment information is missing in convergence block)
   |  
   * commit cc79a1f
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 10 17:10:36 2019 +0200
   | 
   |     Fixed major error in reading convergence blocks!
   |     - gap log and cont status log was read in wrong order
   |     these blocks were read ahead of one iteration
   |     - error was in CONVERGENCE SDI and EQ. blocks starting
   |     they dont start with a phrase 'CONVERGENCE CHECKS FOR'
   |     but with CHECK POINT   START OF SOLVER
   |  
   * commit b0da157
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 10 09:20:39 2019 +0200
   | 
   |     several print functions in comp_items deleted
   |  
   * commit e3cb02c
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 10 09:16:36 2019 +0200
   | 
   |     - None items are now deleted from the listview
   |     ie: when convergence block had missing a moment convergence information
   |     - convergence status algorithm in sta file C/U was updated
   |     Bugs fixed:
   |     - app crashed when used RMB on convergence item when there was wrong model in Ansa
   |     (in showOnlyPartFromNode - ansa_items)
   |  
   * commit eabac08
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Wed Oct 9 15:56:47 2019 +0200
   | 
   |     - Added coloring to C/U lines of the sta file.
   |     - Added LMB and RMB functions on click in listview - convergence
   |     - Redefined search for sets - using NameToEnts ansa fucntion
   |     - Added show only PID when set is not available
   |     - Added unstable contact change items in heuristics
   |     - slightly redefined multiselection in listview - convergence
   |     - redefined U/C status in sta list view
   |     - ctr+a, shift + LMB now works in listview - convergence selection
   |  
   * commit beb325b (tag: V.0.1.1)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Oct 7 13:03:30 2019 +0200
   | 
   |     Minor bugs fixed according to msg files.
   |  
   * commit e88296f
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Oct 7 10:49:50 2019 +0200
   | 
   |     Minor bugs fixed according to msg files.
   |     - ALL MOMENT    RESIDUALS ARE ZERO etc. formulations were missing
   |     - Success -/C/U tweaked
   |  
   * commit 019e18a
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Oct 4 15:09:30 2019 +0200
   | 
   |     Ansa gui updates:
   |     - pick entity was replaced with identify entity - with canvas functions
   |     - added clear canvas button
   |     - multi selection in listview info items was allowed
   |     Parser update:
   |     - in abaqus items
   |     - in abaqusio init item parser was updated with more patterns (1.E-1, 1.2, 1.)
   |  
   * commit 01b861e
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Oct 3 16:23:45 2019 +0200
   | 
   |     Added separate tab in heuristic tab - init gap elements
   |     added new heuristic class in abaqus_items and new block type in the abaqusio
   |     fixed wrong block end in heuristic tab - initial penetrations - whole msg was displayed
   |     - changed how special blocks are terminated during parsing of the msg file (setBlockEnd method)
   |     fixed wrong items displayed in initial penetrations - only overclosers have to be showed
   |       - added deleteBlock method in baseBlock
   |       - this method resets the blockrange to zeroes, so now content is available
   |     fixed multiple lines selection in META in right listview (convergence items)
   |  
   * commit 9581345 (tag: V.0.1.0)
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Wed Oct 2 14:11:18 2019 +0200
   | 
   |     Added untracked abaqus_items.py file to git
   |  
   * commit 59b5b9e
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Wed Oct 2 14:03:02 2019 +0200
   | 
   |     minor bugs fixed:
   |     - pick entities in ansa_items
   |     - show only sets in meta
   |  
   * commit fefc2ff
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Wed Oct 2 08:54:24 2019 +0200
   | 
   |     first testing version, debugged in a1911, m1911
   |     - added ansa_items, meta_items files which contains general ansa/meta functions
   |     - added gap elements
   |     - adding gap elements had impact on the whole parser - ie. new type of string occurs in contact convergence
   |     - debugged show only sets - added hash table for set names, where all ansa/meta sets are stored
   |     - app ported from meta to ansa, identify function was replaced with pickEntities function
   |     - added pick/identify and show only set buttons in heuristics tab
   |  
   * commit d54673f
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Thu Sep 26 15:54:23 2019 +0200
   | 
   |     commit before port to Ansa
   |     added:
   |     - redefined how statistics is shown
   |     - added history to statistics
   |     - added abaqus internal sets read from dat files - redefined dat file parser
   |     - redefined how show only sets works
   |     - added hide/show cols menu to list view widgets
   |     - moved two special block classes from base items to abaqusio, since they become to specific
   |  
   * commit 5201443
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Sep 20 11:27:06 2019 +0200
   | 
   |     added 'zero' line and 'all' line with its content in heur tab
   |     - added new SpecialTypeBlock - SpecialTypeBlockInit in base_items
   |     - added new block 'AbaqusInitWarning(bi.SpecialTypeBlockInit)' (in abaqusio) for initial warnings (initial penetration)
   |     - moved the rest of base items to base_items
   |     fixed bugs:
   |     - line coloring
   |     - redefined if inc has converged or not - added 'U'/'C' or '-' in Success column in navigation widget
   |     - errors when loading other files - added try/except clause in abaqus_items - _setAttributes
   |  
   * commit b4d2f2d
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Sep 16 13:08:42 2019 +0200
   | 
   |     heuristic tab is now filtering the heur. items according to iter. number
   |     heur. tab items now shows if they are empty or not (_checkContent function)
   |     heur. tab items were wrapped in a separate widget (HeuristicNavigationWidget class)
   |     every warning/note/error block has now a placement parameter that poinst to its [step, iteration]
   |     fixed bugs:
   |     - error in statistics node count
   |     - fixed set cursor in text box
   |     - fixed show only sets that were missing (global contact)
   |     - slight perfomance improvements in show only function (collecting sets and elements)
   |  
   * commit 3d28702
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Tue Sep 10 12:03:11 2019 +0200
   | 
   |     commit before heuristic tab edit
   |  
   * commit 0edfc36
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Mon Sep 9 16:34:01 2019 +0200
   | 
   |     control commit - updated Contact status tab, double click behav, message file bg color change on click, etc..
   |  
   * commit f5e49d7
   | Author: Milos Cadek <milos.cadek@idiada.cz>
   | Date:   Fri Aug 30 17:30:35 2019 +0200
   | 
   |     Added coloring to the residual criteria
   |     Added combo boxes with filtering function
   |    
   *   commit ac90238
   |\  Merge: f914f5c 4a25409
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Fri Aug 23 15:27:30 2019 +0200
   | | 
   | |     Merge /data/fem/users/siegl/eclipse/solverOutputAnalysisApp
   | |     Added ansa GUI
   | |     txtio -- BaseBlock class tweaked, added convergence crit parsing
   | |     
   | |     Conflicts:
   | |     	bin/domain/base_items.py
   | |   
   | * commit 4a25409
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Fri Aug 16 17:12:26 2019 +0200
   | | 
   | |     First version of gui for META environment implemented.
   | |   
   * | commit f914f5c
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Mon Aug 19 11:47:21 2019 +0200
   | | 
   | |     clean up in base_items
   | |   
   * | commit 76b9cf8
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Fri Aug 16 11:54:41 2019 +0200
   | | 
   | |     Fixed negative sign read in txtio, updated LABELS in base_items
   | |   
   * | commit f2c1149
   |/  Author: Milos Cadek <milos.cadek@idiada.cz>
   |   Date:   Thu Aug 15 16:43:20 2019 +0200
   |   
   |       Fixed scientific/float problem v1.0
   |    
   *   commit 972b70d
   |\  Merge: e7b7695 3aafa61
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Thu Aug 15 16:23:37 2019 +0200
   | | 
   | |     Merge /data/fem/+software/SKRIPTY/tools/repos/solverOutputAnalysisApp
   | |     
   | |     Conflicts:
   | |     	bin/interfaces/txtio.py
   | |   
   | * commit 3aafa61
   | | Author: Milos Cadek <milos.cadek@idiada.cz>
   | | Date:   Thu Aug 15 15:29:01 2019 +0200
   | | 
   | |     Initial PAMCRASH parser implemented, ABAQUS parser attribute search finished.
   | |   
   * | commit e7b7695
   |/  Author: Milos Cadek <milos.cadek@idiada.cz>
   |   Date:   Thu Aug 15 15:34:36 2019 +0200
   |   
   |       Initial general item structure implemented.
   |  
   * commit 7f97aa6
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Aug 14 09:35:44 2019 +0200
   | 
   |     Empty pamcrashio.py added for BaseParser compatibility check.
   |  
   * commit c65ad20
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Aug 13 13:56:52 2019 +0200
   | 
   |     Initial parser.
   |    
   *   commit 02d7806
   |\  Merge: 95fb024 ad964cf
   | | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | | Date:   Fri Jun 7 12:59:10 2019 +0200
   | | 
   | |     pyProject installer parameters added to ensure future installation consistency.
   | |     
   | |     Conflicts:
   | |     	bin/main.py
   | |   
   | * commit ad964cf (tag: V.0.0.7)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Wed May 22 16:24:09 2019 +0200
   | | 
   | |     small fixations
   | |   
   | * commit 9fb5fdf (tag: V.0.0.6)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Wed May 22 16:12:19 2019 +0200
   | | 
   | |     Support of the pre file
   | |   
   | * commit 2204060 (tag: V.0.0.5)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Fri Apr 26 14:36:26 2019 +0200
   | | 
   | |     small fixes
   | |   
   | * commit 4c683db (tag: V.0.0.4)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Fri Apr 12 17:12:15 2019 +0200
   | | 
   | |     Fix errors ruring analyzing the msg file
   | |   
   | * commit 0da149b (tag: V.0.0.3)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Mon Jan 21 08:20:02 2019 +0100
   | | 
   | |     Was added the colors based on the convergence and gui was modified
   | |   
   | * commit 03ed57d (tag: V.0.0.2)
   | | Author: stekly <jan.stekly@idiada.cz>
   | | Date:   Thu Jan 10 10:40:21 2019 +0100
   | | 
   | |     some minor changes
   | |   
   * | commit 95fb024
   |/  Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   |   Date:   Fri Jun 7 12:53:42 2019 +0200
   |   
   |       Local change save before merge.
   |  
   * commit 4ce8840 (tag: V.0.0.1)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Jan 9 10:47:39 2019 +0100
   | 
   |     First auto installed version.
   |  
   * commit 963c360
     Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
     Date:   Wed Jan 9 10:44:22 2019 +0100
     
         Initial commit.
