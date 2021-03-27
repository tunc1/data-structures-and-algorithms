def sort(array):
    counting=[]
    new_array=[]
    biggest=array[0]
    for item in array:
        if item>biggest:
            biggest=item
        new_array.append(0)
    for _ in range(biggest+1):
        counting.append(0)
    for item in array:
        counting[item]+=1
    for i in range(1,len(counting)):
        counting[i]+=counting[i-1]
    for i in range(len(array)-1,-1,-1):
        new_array[counting[array[i]]-1]=array[i]
        counting[array[i]]-=1
    return new_array