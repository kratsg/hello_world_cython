cimport c_sum_int
from libcpp.vector cimport vector

def sum_int(vector[int] vec): return c_sum_int.sum_int(vec)
