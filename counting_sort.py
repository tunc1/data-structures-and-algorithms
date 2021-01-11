def sort(array):
    string=""
    tmp=[]
    biggest=array[0]
    for item in array:
        if item>biggest:
            biggest=item
    for _ in range(biggest+1):
        tmp.append(0)
    for item in array:
        tmp[item]+=1
    for i,item in enumerate(tmp):
        string+=(str(i)+",")*item
    string=string[:-1]
    return string