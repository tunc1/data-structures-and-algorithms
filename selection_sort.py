def sort(array):
    for i in range(len(array)):
        minimum_index=i
        for j in range(i+1,len(array)):
            if array[minimum_index]>array[j]:
                minimum_index=j
        tmp=array[i]
        array[i]=array[minimum_index]
        array[minimum_index]=tmp
    return array