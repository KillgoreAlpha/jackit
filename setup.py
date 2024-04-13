#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from distutils.core import setup

setup(
    name='JackIt',
    version='0.1.1',
    author='infamy and phikshun',
    packages=['jackit', 'jackit.lib', 'jackit.plugins'],
    scripts=['bin/jackit'],
    url='https://github.com/insecurityofthings/jackit',
    license='BSD',
    description='Exploit framework for MouseJack vulnerability.',
    install_requires=[
        "click==8.1.7",
        "pyusb==1.2.1",
        "tabulate==0.9.0",
        "six==1.16.0"
    ],
)
