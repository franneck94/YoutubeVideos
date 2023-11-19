from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

import numpy


CYTHON_EXTENSION = [
    Extension(
        name='computations2.computations',
        sources=['computations2/computations.pyx'],
        include_dirs=[numpy.get_include()]
    )
]


EXT_MODULES = cythonize(
    CYTHON_EXTENSION,
    compiler_directives={'language_level' : "3"}
)


metadata = dict(
    name="computations2",
    ext_modules=EXT_MODULES,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == '__main__':
    setup_package()
