def find_maxima(list_):
    ind_max = []
    for i, l in enumerate(list_):
        if i == 0:
            if l > list_[i+1]:
                ind_max.append(i)
        if i > 0 and i != (len(list_)-1):
            if l > list_[i-1] and l > list_[i+1]:
                ind_max.append(i)

        if i == (len(list_)-1):
            if l > list_[i-1]:
                ind_max.append(i)
    return ind_max
