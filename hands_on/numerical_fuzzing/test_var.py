from math import isclose
import numpy as np

def test_var_deterministic():
    x = np.array([3.0, 2.1, 6.5])
    guess = np.var(x)

    expected = 3.602

    assert isclose(guess, expected, abs_tol=1e-2)

def test_var_fuzzing():
    x = np.array([3.0, 2.1, 6.5])
    D = len(x)
    N = 100000
    expected = x**2
    random_numbers = np.random.randn(N, D) * x

    assert np.allclose(np.var(random_numbers, axis=0), expected, rtol=1e-2)
