import numpy as np
from math import isclose

def test_mean_deterministic():
    x = np.array([-2.0, 2.0, 6.0])
    expected = float(32/3)
    print(np.var(x))
    assert isclose(np.var(x), expected)

def test_mean_fuzzing():
    rand_state = np.random.RandomState(1333)

    N, D = 100000, 5
    # Goal means: [0.1 ,  0.45,  0.8 ,  1.15,  1.5]
    expected = np.linspace(0.1, 1.5, D)

    # Generate random, D-dimensional data with the desired mean
    x = rand_state.randn(N, D) * np.sqrt(expected)
    vars = np.var(x, axis=0)
    np.testing.assert_allclose(vars, expected, rtol=1e-2)
