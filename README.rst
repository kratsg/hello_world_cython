Installing
==========

.. code::

  $ python setup.py build_ext --inplace
  Compiling example.pyx because it depends on ./c_sum_int.pxd.
  [1/1] Cythonizing example.pyx
  running build_ext
  building 'example' extension
  clang -fno-strict-aliasing -fno-common -dynamic -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I. -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c example.cpp -o build/temp.macosx-10.12-x86_64-2.7/example.o -std=c++11 -stdlib=libc++
  clang -fno-strict-aliasing -fno-common -dynamic -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I. -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c src/example.cpp -o build/temp.macosx-10.12-x86_64-2.7/src/example.o -std=c++11 -stdlib=libc++
  clang++ -bundle -undefined dynamic_lookup build/temp.macosx-10.12-x86_64-2.7/example.o build/temp.macosx-10.12-x86_64-2.7/src/example.o -o /Users/kratsg/hello_world_cython/example.so -std=c++11 -stdlib=libc++

Running
=======

.. code::

  $ python
  Python 2.7.13 (default, Dec 18 2016, 07:03:39)
  [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import hello_world
  Hello World
  >>> import example
  >>> example.sum_int([1,2,3,4])
  10
