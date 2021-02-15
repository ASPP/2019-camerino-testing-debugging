import numpy as np

def local_maxima(numlist):
    #numlist = input('enter list')
    loc = 0
    curr = numlist[0]
    for idx, elem in enumerate(numlist):
        if elem>curr:
            loc = idx
            curr = elem
    print(loc)
    return loc

#local_maxima([1, 3, -1, 2, 1])
#local_maxima([1,4,-5,0,2,1])
#local_maxima([-1,-1,0,1])
