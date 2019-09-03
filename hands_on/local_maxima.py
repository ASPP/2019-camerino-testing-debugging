import numpy as np


def find_maxima(any_list):
    local_minima = []
    for i,item in enumerate(any_list):
        if i == 0:
            if any_list[i+1]<item:
                local_minima.append(i)
        elif i == len(any_list)-1:
            if any_list[i-1]<item:
                local_minima.append(i)
        else:
            if any_list[i-1]<=item>=any_list[i+1]:
                local_minima.append(i)
    return local_minima

def test_find_maxima():
    input = [[1,4,-5,0,2,1],
            [-1,-1,0,-1],
            [4,2,1,3,1,5],
            [1,2,2,1]]
    exp_output = [[1,4],[2],[0,3,5],[1,2]]
    test_res = [find_maxima(k) for k in input]
    if test_res == exp_output:
        print("test passed.")
        pass


if __name__ == "__main__":
    # test_list = [1,2,6,3,4,5]
    # test = find_maxima(test_list)
    # print(test)
    test_find_maxima()
