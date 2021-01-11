def sort(array):
    __sort(array,0,len(array))

def __sort(array,start,end):
    middle=int((start+end)/2)
    if end-start>2:
        __sort(array,0,middle)
        __sort(array,middle,end)
    if end-start>1:
        left_index=start
        right_index=middle
        index=0
        tmp_array=[]
        while left_index<middle and right_index<end:
            if array[left_index]<array[right_index]:
                tmp_array.append(array[left_index])
                left_index+=1
                index+=1
            else:
                tmp_array.append(array[right_index])
                right_index+=1
                index+=1
        while left_index<middle:
            tmp_array.append(array[left_index])
            left_index+=1
            index+=1
        while right_index<end:
            tmp_array.append(array[right_index])
            right_index+=1
            index+=1
        array[start:end]=tmp_array