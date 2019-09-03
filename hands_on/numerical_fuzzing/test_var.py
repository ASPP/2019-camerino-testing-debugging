import numpy as np

def test_var_deterministic():
    x = np.array([1,2,3,4])
    expected = 1.25
    assert np.allclose(np.var(x),expected)
