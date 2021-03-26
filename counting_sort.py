def sort(array):
    tmp=[]
    new_array=[]
    biggest=array[0]
    for item in array:
        if item>biggest:
            biggest=item
    for _ in range(biggest+1):
        tmp.append(0)
    for item in array:
        tmp[item]+=1
    for i,item in enumerate(tmp):
        for _ in range(item):
            new_array.append(i)
    return new_array