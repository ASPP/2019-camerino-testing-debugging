def find_maxima(lst):
    max_index = []
    for index in range(len(lst)):
        if lst[index] > lst[index-1] and lst[index] > lst[index+1]:
            max_index.append(index)
    return max_index

lst = [1,4,-5,0,2,1]
#sst = [-1,-1, 0, -1]
#lst = [4,2,1,3,1,5]

print(find_maxima(lst))
