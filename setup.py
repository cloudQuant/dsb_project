import Cython.Compiler.Options as Cco
import numpy as np
from Cython.Build import cythonize
from setuptools import setup, Extension

import sys


def set_optimize_option(optimize_arg: int) -> str:
    if sys.platform == 'win32':
        return f'/O{optimize_arg}'
    elif sys.platform == 'linux':
        return f'-O{optimize_arg}'
    elif sys.platform == 'darwin':
        return f'-O{optimize_arg}'
    else:
        return f'-O{optimize_arg}'


def set_compile_args(compile_arg: str) -> str:
    if sys.platform == 'win32':
        return f'/{compile_arg}'
    elif sys.platform == 'linux':
        return f'-f{compile_arg}'
    elif sys.platform == 'darwin':
        return f'-O{compile_arg}'
    else:
        return f'-O{compile_arg}'


def set_extra_link_args(link_arg: str) -> str:
    if sys.platform == 'win32':
        return f'/{link_arg}'
    elif sys.platform == 'linux':
        return f'-{link_arg}'
    elif sys.platform == 'darwin':
        return f'-D{link_arg}'
    else:
        return f'-{link_arg}'


def set_cpp_version(cpp_version: str) -> str:
    if sys.platform == 'win32':
        return f'-std:{cpp_version}'
    elif sys.platform == 'linux':
        return f'-std={cpp_version}'
    elif sys.platform == 'darwin':
        return f'-std={cpp_version}'
    else:
        return f'-std={cpp_version}'


# -O3 -march=native
ext = Extension(
    "my_adf", sources=["my_adf.pyx"],
    include_dirs=[np.get_include()],
    language='c++',
    extra_compile_args=[
        set_optimize_option(2),
        # set_compile_args('openmp'),
        # set_compile_args('lpthread'),
        set_cpp_version('c++17'),
        # "-march=native"
    ],
    extra_link_args=[
        set_extra_link_args('lgomp'),
    ]
)

setup(name="my_adf", ext_modules=cythonize([ext]), annotate=True)
