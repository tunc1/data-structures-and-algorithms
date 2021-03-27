def sort(array):
    i=1
    while i<len(array):
        if array[i]<array[i-1]:
            tmp=array[i]
            array[i]=array[i-1]
            array[i-1]=tmp
            if i>1:
                i-=2
        i+=1
    return array