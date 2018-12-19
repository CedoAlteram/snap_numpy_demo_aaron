#!/usr/bin/env python3

from setuptools import setup

setup(
   name='snap-numpy-aaron',
   version='1.0',
   description='simple snap / numpy demo',
   author='aaron',
   author_email='aaron@fake_email.com',
   packages=['snap_numpy'],
   scripts=['bin/snap_numpy_aaron.py'],
   install_requires=['numpy'],
)
