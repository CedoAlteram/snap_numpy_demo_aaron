#!/usr/bin/env python3

from setuptools import setup


setup(
    name='snap-numpy-aaron',
    version='1.0',
    author='aaron',
    author_email='aaron@fake_email.com',
    description='simple snap / numpy demo',
    url='https://github.com/varUP/snap_numpy_demo_aaron.git',
    packages=['snap-numpy-aaron'],
    scripts=['bin/snap_numpy_aaron.py'],
    install_requires=['numpy'],
    license='License :: MIT License',
)
