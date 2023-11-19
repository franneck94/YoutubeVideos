from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize


CYTHON_EXTENSION = [
    Extension(
        name='primes1.primes',
        sources=['primes1/primes.pyx'],
    )
]


EXT_MODULES = cythonize(CYTHON_EXTENSION, language_level="3")


metadata = dict(
    name="primes1",
    ext_modules=EXT_MODULES,
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == '__main__':
    setup_package()
