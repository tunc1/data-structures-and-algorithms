def search(array,item):
    for i in range(len(array)):
        if array[i]==item:
            return i
    return -1