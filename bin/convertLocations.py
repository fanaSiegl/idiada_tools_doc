#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''


'''


#==============================================================================

import os
import sys
import re

from domain import utils

#==============================================================================

def fixLocation(fileName, location):
    
    fi = open(fileName, 'rt')
    lines = fi.readlines()
    fi.close()
    
    locationIndex = lines[0].find(': ./')+4
    if not lines[0][locationIndex:].startswith(location):
        newLine = lines[0][:locationIndex] + '%s/' % location + lines[0][locationIndex:]
        lines[0] = newLine
        
        fo = open(fileName, 'wt')
        for line in lines:
            fo.write(line)
        fo.close()
        
    
#==============================================================================

def convertLocations():
    
    for location in utils.getListOfLocations():
        path = os.path.join(utils.SPHINX_SOURCE, location) 
        if os.path.isdir(path):
            print(path, location)
            for root, dirs, files in os.walk(path):
                for name in files:
                    if name.endswith('.txt'):
                        fileName = os.path.join(root, name)
                        fixLocation(fileName, location)

#=============================================================================

if __name__ == '__main__':
    
    convertLocations()