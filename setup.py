#!/usr/bin/env python

from distutils.core import setup

def read(relative):
    """
    Read file contents and return a list of lines.
    ie, read the VERSION file
    """
    contents = open(relative, 'r').read()
    return [l for l in contents.split('\n') if l != '']


setup(name='filldrive',
      version='1.0',
      description='This program creates a number of file with certain size automatically',
      author='Dell | EMC',
      install_requires=read('./requirements.txt'),
      url='https://github.com/open4storage/filldrive'
     )
