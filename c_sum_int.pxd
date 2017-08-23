from libcpp.vector cimport vector

# Define your function as you need.
cdef extern from "src/example.hpp":
  int sum_int(vector[int] vec)
