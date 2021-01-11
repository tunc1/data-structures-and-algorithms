def search(array,item):
    return __search(array,item,0,len(array))

def __search(array,item,start,end):
    if end-start>1:
        middleIndex=int((start+end)/2)
        middle=array[middleIndex]
        if middle<item:
            return __search(array,item,middleIndex+1,len(array))
        elif middle>item:
            return __search(array,item,0,middleIndex)
        else:
             return middleIndex
    else:
        if array[start]==item:
            return start
        else:
            return -1
