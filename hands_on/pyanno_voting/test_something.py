from math import isclose
import numpy
#from numpy import assert_array_equal

def test_floating():
    assert isclose(1.1 + 2.2, 3.3)

#def test_tol():
#    assert isclose(1.1 + 2.2, abs_tol=0.1)

def test_arraysum():
    x = numpy.array([1,1])
    y = numpy.array([2,2])
    z = numpy.array([3,3])
    assert all(x + y == z)
    #assert_array_equal(x + y, z)


def test_arithmetic():
    assert 1 == 1
    assert 2 * 3 == 6

def test_len_list():
    lst = ['a', 'b', 'c']
    assert len(lst) == 3

def test_equalthree():
    assert 1 + 2 == 3

def test_truthy():
    assert 1

#def test_floatsum():
#    assert 1.1 + 2.2 == 3.3
