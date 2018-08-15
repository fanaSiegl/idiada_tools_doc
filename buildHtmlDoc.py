#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

#===============================================================================

PATH_SELF = os.path.dirname(os.path.realpath(__file__))
PATH_SOURCE = os.path.join(PATH_SELF, 'source')

OUTPUT_NAME = 'index.rst'

HEADER = '''IDIADA script documentation
===========================

.. toctree::
   :maxdepth: 2

'''

FOOTER = '''
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`'''

#===============================================================================

def getToolGroupString(groupName):
    
    if '_' in groupName:
        groupName = groupName.replace('_',' ')
    
    string = '\n%s\n' % groupName
    string += len(groupName)*'-' + '\n'
    return string

#===============================================================================

def getDocFileContent(path):
    
    fi = open(path, 'rt')
    lines = ''.join(fi.readlines())
    fi.close()
    
    return lines
    

#=============================================================================

def main():
    
    content = HEADER
    
    for item in os.listdir(PATH_SOURCE):
        if os.path.isdir(os.path.join(PATH_SOURCE, item)):
            content += getToolGroupString(item)
            for toolDocFileName in os.listdir(os.path.join(PATH_SOURCE, item)):
                toolDocPath = os.path.join(PATH_SOURCE, item, toolDocFileName)
                content += getDocFileContent(toolDocPath)

    content += FOOTER
    
    fo = open(os.path.join(PATH_SOURCE, OUTPUT_NAME), 'wt')
    fo.write(content)
    fo.close()
    
    os.system('sphinx-build -b html -d build/doctrees   source build/html')

    print "Build finished."
       
#=============================================================================

if __name__ == '__main__':
    
    main()