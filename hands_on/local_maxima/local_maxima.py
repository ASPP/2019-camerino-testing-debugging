import numpy as np


def find_maxima(numbers):
    local_maxima = []
    for i,number in enumerate(numbers):
        if i == 0:
            if number > numbers[i+1]:
                local_maxima.append(number)
        elif i == len(numbers)-1:
            if number > numbers[i-1]:
                local_maxima.append(number)
        else:
            if number > numbers[i-1] and number > numbers[i+1]:
                local_maxima.append(number)
    return local_maxima

print(find_maxima([5,4,-3,-2,7,4,4,8]))
