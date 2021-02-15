import numpy as np
import random
from math import isclose


def test_var_deterministic():
     # Given
     input = [0, 1, 2, 3]
     expected = 1.25

     # When
     result = np.var(input)

     # Then
     assert isclose(result, expected, abs_tol=0.01)


def test_var_fuzzy():
    # Given
    expected = 5
    input = [random.gauss(0, np.sqrt(expected)) for i in range(100000)]

    # When
    result = np.var(input)

    # Then
    assert isclose(result, expected, abs_tol=0.05)
