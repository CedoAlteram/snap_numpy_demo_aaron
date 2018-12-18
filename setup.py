#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup

package_name = 'snap-numpy-aaron'


setup(
    name='snap-numpy-aaron',
    version='1.0.0',
    author='aaron',
    author_email='aaron@fake_email.com',
    description='simple snap / numpy demo',
    url='',
    py_modules=[package_name],
    scripts=['bin/snap-numpy-aaron.py'],
    install_requires=['numpy'],
    license='License :: MIT License',
)
