import numpy as np


def find_maxima(any_list):
    maxlist=np.max(any_list)
    return maxlist

if __name__ == "__main__":
    test_list = np.asarray([1,2,3,4,5])
    test = find_maxima(test_list)
    print(test)
