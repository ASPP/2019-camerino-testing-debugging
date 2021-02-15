#Create a directory called numerical_fuzzing in hands_on.
#In a module called test_var.py, write two tests for the variance function, numpy.var:
#    First, a deterministic test
#    Then, a numerical fuzzing test
from math import isclose
import numpy
from numpy import testing

def test_var_deterministic():
    x = numpy.array([-2.0, 2.0, 6.0])
    expected = 10.6
    assert isclose(numpy.var(x), expected, abs_tol = 0.1)

def test_var_fuzzing():
    rand_state = numpy.random.RandomState(1333)
    N, D = 100000, 5
    #Goal var: [0.1 , 0.45, 0.8 , 1.15, 1.5]
    expected = numpy.linspace(0.1, 1.5, D)
    # Generate random, D-dimensional data with the desired mean
    x = rand_state.randn(N, D) * expected
    vars = numpy.var(x, axis=0)
    numpy.testing.assert_allclose(vars, expected*expected, rtol=1e-2)
