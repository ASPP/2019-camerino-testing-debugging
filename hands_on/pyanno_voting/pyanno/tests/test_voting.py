import numpy as np

from pyanno import voting
from pyanno.voting import MISSING_VALUE as MV

from math import isclose


def test_labels_count():
    #given
    annotations = [
        [1,  2, MV, MV],
        [MV, MV,  3,  3],
        [MV,  1,  3,  1],
        [MV, MV, MV, MV],
    ]
    nclasses = 5
    expected = [0, 3, 1, 3, 0]

    #when
    result = voting.labels_count(annotations, nclasses)

    #then
    assert result == expected


def test_labels_frequency():
    #given
    matrix = [
        [1, 2, 2, -1],
        [2, 2, 2, 2],
        [1, 1, 3, 3],
        [1, 3, 3, 2],
        [-1, 2, 3, 1],
        [-1, -1, -1, 3],
    ]

    matrix2 = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1]
    ]

    lowerlimit = 0
    upperlimit = 1
    nclasses = 4
    
    expected2 = np.zeros(nclasses)


    #when
    result = voting.labels_frequency(matrix, nclasses)
    result2 = voting.labels_frequency(matrix2, nclasses)

    #then
    assert np.all([res != None for res in result])
    assert len(result) == nclasses
    assert np.all(result2 == expected2)
    assert np.all([i >= lowerlimit and i <= upperlimit for i in result])
    assert isclose(np.sum(result),upperlimit) or isclose(np.sum(result), lowerlimit,abs_tol=1e-12)


def test_majority_vote():
    annotations = [
        [1, 2, 2, MV],
        [2, 2, 2, 2],
        [1, 1, 3, 3],
        [1, 3, 3, 2],
        [MV, 2, 3, 1],
        [MV, MV, MV, 3],
    ]
    expected = [2, 2, 1, 3, 1, 3]
    result = voting.majority_vote(annotations)
    assert result == expected


def test_majority_vote_empty_item():
    # Test for former bug: majority vote with row of invalid annotations fails
    annotations = np.array(
        [[1, 2, 3],
         [MV, MV, MV],
         [1, 2, 2]]
    )
    expected = [1, MV, 2]
    result = voting.majority_vote(annotations)
    assert result == expected
