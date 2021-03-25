def sort(array):
    j=0
    while True:
        has_changed=False
        for i in range(len(array)-1-j):
            if array[i]>array[i+1]:
                tmp=array[i]
                array[i]=array[i+1]
                array[i+1]=tmp
                has_changed=True
        if not has_changed:
            break
        j+=1
    return array