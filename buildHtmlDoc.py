#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

#===============================================================================

SPHINX_DOC = os.path.dirname(os.path.realpath(__file__))
SPHINX_SOURCE = os.path.join(SPHINX_DOC, 'source')
SPHINX_DOCTREES = os.path.join(SPHINX_DOC, 'build', 'doctrees')
SPHINX_HTML = os.path.join(SPHINX_DOC, 'build', 'html')

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
    
    for item in os.listdir(SPHINX_SOURCE):
        if os.path.isdir(os.path.join(SPHINX_SOURCE, item)):
            content += getToolGroupString(item)
            for toolDocFileName in os.listdir(os.path.join(SPHINX_SOURCE, item)):
                toolDocPath = os.path.join(SPHINX_SOURCE, item, toolDocFileName)
                content += getDocFileContent(toolDocPath)

    content += FOOTER
    
    fo = open(os.path.join(SPHINX_SOURCE, OUTPUT_NAME), 'wt')
    fo.write(content)
    fo.close()
    
    # create local documentation
    os.system('sphinx-build -b html -d %s %s %s' % (SPHINX_DOCTREES, SPHINX_SOURCE, SPHINX_HTML))
    
    print "Build finished."
       
#=============================================================================

if __name__ == '__main__':
    
    main()