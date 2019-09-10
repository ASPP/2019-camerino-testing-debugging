# Importing libraries required
import numpy as np
from math import isclose
from numpy.testing import assert_allclose

# deterministic test
def test_var_deterministic():
    # Given
    x = np.array([1,2,3,4])
    expected_var = 1.25

    # When
    calculated_variance = x.var()

    # Then
    assert isclose(x.var(), expected_var)


# numerical fuzzing test
def test_var_fuzzing():
    # Setting the seed for random values generators
    rand_state = np.random.RandomState(20000)

    # Defining rows and columns for the array
    N, D = 100, 4

    # Defining expected variances (we choose them as we want)
    expected = np.linspace(0.4, 1.2, D)

    # Generating random values N(0,1) biased with variance
    x = rand_state.randn(N, D) * np.sqrt(expected)

    variances = np.var(x, axis=0)

    np.testing.assert_allclose(variances, expected, rtol=5e-1)
