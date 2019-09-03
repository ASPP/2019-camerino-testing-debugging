import numpy as np
from math import isclose

def test_var_determistic():
    arr = np.array([1,2,3,4,3,2,1])
    expected = 1.0612244897959184
    result = np.var(arr)
    assert isclose(result, expected)

def test_var_fuzzing():

    size = 100000
    variance = 1.5
    arr = np.random.normal(size = size, scale = np.sqrt(variance))
    expected = 1.5
    result = np.var(arr)
    assert isclose(result, expected, abs_tol =0.1)
