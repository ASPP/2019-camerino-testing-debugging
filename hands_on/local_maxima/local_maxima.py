def find_maxima(input):

    output = []

    for i,v in enumerate(input[1:-1]):

        if (v>input[i]) and (v>input[i+2]):

            output.append(i+1)

    return(output)

print(find_maxima([1,4,-5,0,2,1]))
print(find_maxima([-1,-1,0,-1]))

print('end')