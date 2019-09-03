import numpy as np
from math import isclose

def test_var_deterministic():
    x = np.array([0.0, 1.0, 2.0, 3.0])
    print(np.var(x))
    expected = 1.25
    assert isclose(np.var(x), expected)


def test_var_fuzzing():
    rand_state = np.random.RandomState(1333)

    N, D = 100000, 5
    # Goal means: [0.1 ,  0.45,  0.8 ,  1.15,  1.5]
    testdata = np.linspace(0.1, 1.5, D)
    expected = np.ones(D)
    # Generate random, D-dimensional data with the desired mean
    x = rand_state.randn(N, D) + testdata
    vars = np.var(x, axis=0)
    np.testing.assert_allclose(vars, expected, rtol=1e-2)
