from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

setup(
  name='hello_world_cython',
  ext_modules=cythonize([
    Extension('hello_world', sources=['hello_world.pyx'], language='c++'),
    Extension('example', sources=['example.pyx', 'src/example.cpp'], language='c++', extra_compile_args=["-std=c++11","-stdlib=libc++"], extra_link_args=["-std=c++11","-stdlib=libc++"])
  ])
)
