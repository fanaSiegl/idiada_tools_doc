#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Python script for '''

import os
import sys
import configparser
import numpy as np
import subprocess

#==============================================================================

PATH_BIN = os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),'..'))
PATH_INI = os.path.normpath(os.path.join(PATH_BIN,'..', 'ini'))
PATH_DOC = os.path.normpath(os.path.join(PATH_BIN,'..', 'doc'))
PATH_RES = os.path.normpath(os.path.join(PATH_BIN,'..', 'res'))
PATH_ICONS = os.path.join(PATH_RES, 'icons')

SPHINX_SOURCE = os.path.join(PATH_RES, 'source')
SPHINX_DOCTREES = os.path.join(PATH_RES, 'build', 'doctrees')
SPHINX_HTML = os.path.join(PATH_RES, 'build', 'html')
    
OUTPUT_NAME = 'index.rst'
CONFIG_FILE = 'config.ini'    
VERSION_FILE = 'version.ini'

#==============================================================================

def getVersionInfo():

    SECTION_VERSION = 'VERSION'
     
    config = configparser.ConfigParser()
     
    cfgFileName = os.path.join(PATH_INI, VERSION_FILE)
    config.read(cfgFileName)
         
    revision = config.get(SECTION_VERSION, 'REVISION')
    modifiedBy = config.get(SECTION_VERSION, 'AUTHOR')
    lastModified = config.get(SECTION_VERSION, 'MODIFIED')
 
    return revision, modifiedBy, lastModified

#==============================================================================

def runSubprocess(command, cwd=None):
    
    process = subprocess.Popen(
        command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        cwd=cwd)
    
    return process.communicate()

#==============================================================================

def getLocalLocation():
         
    config = configparser.ConfigParser()
    
    cfgFileName = os.path.join(PATH_INI, CONFIG_FILE)
    config.read(cfgFileName)
    
    return config['GENERAL']['LOCAL_DOCUMENTATION']

#==============================================================================

def getListOfLocations():
         
    config = configparser.ConfigParser()
    
    cfgFileName = os.path.join(PATH_INI, CONFIG_FILE)
    config.read(cfgFileName)
    
    locations = config['GENERAL']['LOCATIONS'].split(',')
    return [location.strip() for location in locations] 

#==============================================================================
    