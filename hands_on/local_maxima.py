import numpy as np


def find_maxima(any_list):
    local_minima = []
    for i,item in enumerate(any_list):
        if i == 0:
            if any_list[i+1]<item:
                local_minima.append(item)
        elif i == len(any_list)-1:
            if any_list[i-1]<item:
                local_minima.append(item)
        else:
            if any_list[i-1]<item>any_list[i+1]:
                local_minima.append(item)
    return local_minima

if __name__ == "__main__":
    test_list = [1,2,6,3,4,5]
    test = find_maxima(test_list)
    print(test)
