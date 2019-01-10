#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

#===============================================================================

SPHINX_DOC = os.path.dirname(os.path.realpath(__file__))
SPHINX_SOURCE = os.path.join(SPHINX_DOC, 'source')
SPHINX_DOCTREES = os.path.join(SPHINX_DOC, 'build', 'doctrees')
SPHINX_HTML = os.path.join(SPHINX_DOC, 'build', 'html')
SPHINX_BUILD = os.path.join(SPHINX_DOC, 'sphinx-build.py')

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

SPHINX_SECTION_HIERARCHY = ['-', '^', '"']

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

def analyseLevel(newLevel):
    
    
    
    section = ''
    for level, levelName in enumerate(newLevel):
        
        levelName = levelName.replace('_', ' ')
        if levelName not in sectionsCreated:
            section += '%s\n' % levelName
            section += '%s\n' % str(len(levelName)*SPHINX_SECTION_HIERARCHY[level])
            
            sectionsCreated.append(levelName)
                
    return section

#=============================================================================

sectionsCreated = list()

#=============================================================================

def main():
    
    content = HEADER
    dirStructure = list()
    for root, dirs, files in os.walk(SPHINX_SOURCE, topdown=True):
        for name in files:
            fileExt = os.path.splitext(name)[1]
            if fileExt == '.txt':
                toolDocPath = os.path.join(root, name)
                dirStructure = toolDocPath.replace(SPHINX_SOURCE, '')
                dirStructure = dirStructure.replace(name, '')
                parts = dirStructure.split(os.path.sep)
                dirStructure = [part for part in parts if len(part) > 0]

                levelName = analyseLevel(dirStructure[:-1])
                content += levelName
                content += getDocFileContent(toolDocPath)
    
#     content += FOOTER
    
    fo = open(os.path.join(SPHINX_SOURCE, OUTPUT_NAME), 'wt')
    fo.write(content)
    fo.close()
     
    # create local documentation
    os.system('python %s -b html -d %s %s %s' % (
        SPHINX_BUILD, SPHINX_DOCTREES, SPHINX_SOURCE, SPHINX_HTML))
    
    print "Build finished."
       
#=============================================================================

if __name__ == '__main__':
    
    main()