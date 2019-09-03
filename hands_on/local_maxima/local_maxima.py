def local_maxima(x):
    local_max_list = []
    for i in range(len(x)):
        if i==0:
            pass
        elif i>0:
            diff=x[i]-x[i-1]
            if diff<0:
                local_max_list.append(x[i-1])
            else:
                pass
