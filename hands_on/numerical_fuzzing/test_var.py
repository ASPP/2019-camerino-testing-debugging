import numpy as np

def test_var_deterministic():
    x = np.array([1,2,3,4])
    expected = 1.25
    assert np.allclose(np.var(x),expected)

def test_var_fuzzing():
    expected = 1.25
    x = np.random.randn(10000000,1) * np.sqrt(expected)

    assert np.isclose(np.var(x), expected, rtol=1e-02)
