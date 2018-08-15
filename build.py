#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Python script for '''

import os
import sys
import shutil
import subprocess
import argparse

PATH_SELF = os.path.dirname(os.path.abspath(__file__))

#===============================================================================

def runSubprocess(command):
    
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    return process.communicate()

    
#=============================================================================

def createRevisionContents():
    
    print 'Creating a revision content'
    
    if os.path.isdir(targetDir):
        print 'Current revision exists already.'
        sys.exit()
    else:
        os.makedirs(targetDir)
    
    runSubprocess('git clone . %s' % (targetDir))
    runSubprocess('git checkout %s' % (args.revision))

#=============================================================================

def cleanUp():
    
    print 'Cleaning up files'
    
    repositoryPath = os.path.join(targetDir, '.git')
    shutil.rmtree(repositoryPath)
    
    repositoryPath = os.path.join(targetDir, '.gitignore')
    os.remove(repositoryPath)
        
    buildScript = os.path.join(targetDir, 'build.py')
    os.remove(buildScript)

    
#=============================================================================

def getRevisionInfo():
    
    print 'Gathering revision information'
    
    output, _ = runSubprocess('git log %s -n 1' % args.revision)
    
    lines = output.split('\n')
    
    modifiedBy = lines[1].split(':')[1].strip()
    lastModified = ':'.join(lines[2].split(':')[1:]).strip()
    
    return modifiedBy, lastModified

#=============================================================================

def install():
    
    print 'Releasing to the productive version'
    
    defaultDir = os.path.join(args.target, 'default')
    
    if os.path.exists(defaultDir):
        os.unlink(defaultDir)
    os.symlink(args.revision, defaultDir)
    
#=============================================================================
    
parser = argparse.ArgumentParser(description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('target', help='Build destination path.')
parser.add_argument('revision', help='Revision number to be build.')
parser.add_argument('-i', action='store_true',  dest='install',
    help='Makes a build revision default.')

args = parser.parse_args()

targetDir = os.path.join(args.target, args.revision)

createRevisionContents()
modifiedBy, lastModified = getRevisionInfo()
cleanUp()

if args.install:
    install()
    
print 'Done'