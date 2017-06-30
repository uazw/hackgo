#!/usr/bin/env python

'''
setup script
'''

from setuptools import setup

setup(name='hackgo',
      version='1.0',
      description='auto-scale go agent base on waiting jobs',
      packages=['hackgo'],
      install_requires=[
          'requests',
          'beautifulsoup4'],
      test_suite='nose.collector',
      tests_require=['nose'])
