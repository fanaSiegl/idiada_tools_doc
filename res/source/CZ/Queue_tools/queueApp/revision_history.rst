
Revision history
================

Revision history graph::
    
       * commit d0984b0 (HEAD, tag: V.0.1.11, origin/master, origin/HEAD, master)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Apr 8 13:48:04 2020 +0200
   | 
   |     TOSCA support implemented. Recursive include search implemented.
   |  
   * commit 5eaa0f7 (tag: V.0.1.10)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu Feb 6 10:26:45 2020 +0100
   | 
   |     ABAQUS INPUT PASSWORD keyword skipped and include check performed.
   |  
   * commit 18d0cff
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Feb 5 19:07:02 2020 +0100
   | 
   |     USER bug fix..
   |  
   * commit 190355f
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Feb 5 18:51:04 2020 +0100
   | 
   |     License restriction settings added.
   |  
   * commit 81a75e5
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Feb 5 18:32:18 2020 +0100
   | 
   |     License restrictions implemented. Configuration is stored in config.ini file and settings is possible via "Settings" menu available for defined users.
   |  
   * commit aa9864d (tag: V.0.1.9)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Jan 28 09:38:43 2020 +0100
   | 
   |     updated version
   |  
   * commit e2fd2f3
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Jan 28 09:36:29 2020 +0100
   | 
   |     Input file selection treeview item selection improved (ctrl+A bug fixed)
   |  
   * commit f1917ea
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jan 27 12:11:12 2020 +0100
   | 
   |     Version update according to requested changes from TODO list.
   |  
   * commit d9d5fc3
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jan 27 12:06:30 2020 +0100
   | 
   |     Small changes from TODO list implemented (#40, #42, #51, #53), input file selection treeview changed to display file system tree instead of a list of files.
   |  
   * commit c68bb09 (tag: V.0.1.8)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Dec 2 11:33:58 2019 +0100
   | 
   |     ABAQUS includes with password skipped.
   |  
   * commit e91e7df
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Dec 2 11:28:24 2019 +0100
   | 
   |     ABAQUS includes with password skipped during the include existance check.
   |  
   * commit 3584f15 (tag: V.0.1.7)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu Aug 29 14:26:16 2019 +0200
   | 
   |     Post-processing bug fix. When submitting multiple jobs, post-processing *.sh code was not updated according to the particular job name.
   |  
   * commit 658d69c (tag: V.0.1.6)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu Aug 15 14:40:30 2019 +0200
   | 
   |     multiple hard_reguest attributes in random order dirty bug fix:(
   |  
   * commit e3bb931 (tag: V.0.1.5)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Aug 5 15:38:04 2019 +0200
   | 
   |     Resource hard requests implemented. ABAQUS restart bug fixed.
   |  
   * commit 380d846
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Aug 5 15:21:16 2019 +0200
   | 
   |     New resource hard requests implemented, ABAQUS job restart bug fixed.
   |  
   * commit 33e520e
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Aug 5 08:29:19 2019 +0200
   | 
   |     hard request implemented. Restart for ABAQUS bug fixed (missing parameter added to *.sh).
   |  
   * commit 582b431
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri Jul 19 14:11:23 2019 +0200
   | 
   |     Disappearing out-of-the-queue jobs bug fixed, job running in an unknown queue ignored..
   |  
   * commit ea5cb12 (tag: V.0.1.4)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Jul 17 11:46:05 2019 +0200
   | 
   |     ABAQUS profile restrictions implemented, qq update set to 10s, human readable (hr) queue_name attribute added, dft postprocessing types changed.
   |  
   * commit 8f683ba (tag: V.0.1.3)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Jul 10 09:23:35 2019 +0200
   | 
   |     Sleeping while file lock bug fixed for ABSAQUS.
   |  
   * commit eaaae7a (tag: V.0.1.2)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jul 8 18:12:20 2019 +0200
   | 
   |     Submit not in current direcotry bug fixed, mailing option set to "-m beas", job monitor bug fixed.
   |  
   * commit 7764651 (tag: V.0.1.1)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Jul 3 16:29:26 2019 +0200
   | 
   |     QUEUE_CODE bug fixed, PAMCRASH relative path of includes check bug fixed, "$?" - return status added.
   |  
   * commit 68f5d56 (tag: V.0.1.0)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jun 17 13:38:58 2019 +0200
   | 
   |     Images add to documentation.
   |  
   * commit ea074d1
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jun 17 13:07:32 2019 +0200
   | 
   |     Postprocessing enabled for all solvers.
   |  
   * commit 174e18d
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jun 17 12:15:29 2019 +0200
   | 
   |     First productive version (Implementation Request No: 10, 12, 15, 16, 17, 18)
   |  
   * commit 6a272a0
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Jun 17 11:59:00 2019 +0200
   | 
   |     PAMCRASH datacheck key word added automatically to the *.pc file based on selected profile.
   |  
   * commit b0e6d39
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri Jun 14 12:15:14 2019 +0200
   | 
   |     TreeView for queue implemented, dynamic loading of META postprocessing types implemented.
   |  
   * commit 66a6896
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri May 31 17:25:56 2019 +0200
   | 
   |     TOSCA submission implementation in progress..
   |  
   * commit 23a3dc2
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri May 31 15:57:00 2019 +0200
   | 
   |     selector itmes and profile items moved to separate modules.
   |  
   * commit 4f7c916
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu May 30 15:57:20 2019 +0200
   | 
   |     NASTRAN submission implemented.
   |  
   * commit 0568fe3
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed May 29 16:49:48 2019 +0200
   | 
   |     New UNKNOWN solver type added; Resource priority profiles 1,2,3 added for ABAQUS; postprocessing type selection implemented; q: jobs sorting according to solver implemented.
   |  
   * commit feaf0c5 (tag: V.0.0.9)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue May 28 13:13:39 2019 +0200
   | 
   |     PAMCRASH V2016.06 option added to qq, solver selection option added to qp.
   |  
   * commit e6044dd
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue May 28 12:44:14 2019 +0200
   | 
   |     PAMCRASH V2016.06 option added, qp extended of solver selection option.
   |  
   * commit 761adc9
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Apr 24 15:35:13 2019 +0200
   | 
   |     so-4 added. Check for further warining added.
   |  
   * commit 9ab491e (tag: V.0.0.8)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Apr 24 09:53:36 2019 +0200
   | 
   |     PamCrash submitting command bug fixed.
   |  
   * commit 001e878
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Apr 24 09:49:14 2019 +0200
   | 
   |     pamcrash submit command *.pc suffix bug fixed.
   |  
   * commit e102736
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu Mar 21 16:25:20 2019 +0100
   | 
   |     File content tracking changed to tail.
   |  
   * commit 27d6f23 (tag: V.0.0.7)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Thu Mar 21 14:27:30 2019 +0100
   | 
   |     Documentation added. Job progress monitoring added.
   |  
   * commit 712394e (tag: V.0.0.6)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Mar 20 13:56:25 2019 +0100
   | 
   |     Test version with parametric input interface.
   |  
   * commit 55ad075
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Mar 20 13:52:48 2019 +0100
   | 
   |     Parametric interface for qaba and qpam implemented.
   |  
   * commit 0b99707 (tag: V.0.0.5)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Mar 19 17:24:22 2019 +0100
   | 
   |     Logging implemented. Different levels are printed out based on application interface type.
   |  
   * commit 3593f55
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Mar 19 17:10:05 2019 +0100
   | 
   |     logging implemented.
   |  
   * commit 8a4997d
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Mar 19 16:22:37 2019 +0100
   | 
   |     Running jobs order fixed, out of the queue running jobs displaying bug fixed.
   |  
   * commit a46e6da
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Mar 19 15:01:05 2019 +0100
   | 
   |     Updating qq queue bug fixed.
   |  
   * commit 2e3f14a
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Tue Mar 19 14:19:37 2019 +0100
   | 
   |     Job terminate, jobs running out of the queue implemented.
   |  
   * commit 418f548 (tag: V.0.0.4)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Mar 18 15:41:53 2019 +0100
   | 
   |     DEBUG param moved to application in order to be propagated to the whole data structure.
   |  
   * commit 7387c2d
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Mon Mar 18 15:27:20 2019 +0100
   | 
   |     Debug option influence to qsub implemented.
   |  
   * commit c5e7876 (tag: V.0.0.3)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri Mar 15 17:08:11 2019 +0100
   | 
   |     Missing module added.
   |  
   * commit 68a5eb9
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri Mar 15 16:48:16 2019 +0100
   | 
   |     First gui version implemented.
   |  
   * commit a26e5d0 (tag: V.0.0.2)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Fri Mar 8 13:12:04 2019 +0100
   | 
   |     qa - submit abaqus, qp - submit pamcrash, q - list of running jobs
   |  
   * commit 7764875 (tag: V.0.0.1)
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Mar 6 17:16:02 2019 +0100
   | 
   |     Test version.
   |  
   * commit 7968830
   | Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
   | Date:   Wed Mar 6 16:50:43 2019 +0100
   | 
   |     First test version. Multi-file submition implemented, profiles implemented.
   |  
   * commit 1bf613c
     Author: Frantisek Siegl <frantisek.siegl@idiada.cz>
     Date:   Fri Mar 1 12:33:24 2019 +0100
     
         Initial commit.
