#!/usr/bin/python2.7

"setup.py script"

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

ext_modules = [Extension("life_cy",sources =  ["life_cy.pyx","life.c"],headers = ["life.h"], include_dirs = [numpy.get_include()],pyrex_gdb=True, extra_compile_args=["-std=c99", "-O3", "-g"]) ]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

