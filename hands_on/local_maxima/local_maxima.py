#creqte a function thqt finds locql maxima

def find_maxima(listOfNumbers):
    localMaxima = []
    for i,num in enumerate(listOfNumbers):
        if i>0 and i<len(listOfNumbers)-1:
            if listOfNumbers[i-1] < num and listOfNumbers[i+1] < num:
                localMaxima.append(i)
    return localMaxima
