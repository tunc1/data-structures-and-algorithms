def sort(array):
    for i in range(1,len(array)):
        j=0
        while i-j>0 and array[i-j]<array[i-j-1]:
            tmp=array[i-j]
            array[i-j]=array[i-j-1]
            array[i-j-1]=tmp
            j+=1
    return array