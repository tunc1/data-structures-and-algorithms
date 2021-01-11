class MaxHeap:
    
    def __init__(self):
        self.__array=[]

    def insert(self,data):
        self.__array.append(data)
        if len(self.__array)>1:
            latest_index=len(self.__array)-1
            self.__check_after_insert(latest_index)
    
    def remove(self):
        tmp=self.__array[0]
        self.__array[0]=self.__array[-1]
        del self.__array[-1]
        self.__check_after_remove(0)
        return tmp
    
    def __check_after_remove(self,index):
        item=self.__array[index]
        if index*2+2<len(self.__array):
            right_child=self.__array[index*2+2]
            left_child=self.__array[index*2+1]
            if right_child>left_child:
                biggest_child=right_child
                biggest_child_index=index*2+2
            else:
                biggest_child=left_child
                biggest_child_index=index*2+1
            if item<biggest_child:
                self.__array[index],self.__array[biggest_child_index]=self.__array[biggest_child_index],self.__array[index]
                self.__check_after_remove(biggest_child_index)
        elif index*2+1<len(self.__array)-1:
            left_child=self.__array[index*2+1]
            if left_child>item:
                self.__array[index],self.__array[index*2+1]=self.__array[index*2+1],self.__array[index]
                self.__check_after_remove(index*2+1)

    def __check_after_insert(self,index):
        parent_index=int((index-1)/2)
        item=self.__array[index]
        parent=self.__array[parent_index]
        if parent<item:
            self.__array[index],self.__array[parent_index]=self.__array[parent_index],self.__array[index]
            self.__check_after_insert(parent_index)
    
    def __str__(self):
        return str(self.__array)

class MinHeap:
    
    def __init__(self):
        self.__array=[]

    def insert(self,data):
        self.__array.append(data)
        if len(self.__array)>1:
            latest_index=len(self.__array)-1
            self.__check_after_insert(latest_index)
    
    def remove(self):
        tmp=self.__array[0]
        self.__array[0]=self.__array[-1]
        del self.__array[-1]
        self.__check_after_remove(0)
        return tmp
    
    def __check_after_remove(self,index):
        item=self.__array[index]
        if index*2+2<len(self.__array):
            right_child=self.__array[index*2+2]
            left_child=self.__array[index*2+1]
            if right_child<left_child:
                smallest_child=right_child
                smallest_child_index=index*2+2
            else:
                smallest_child=left_child
                smallest_child_index=index*2+1
            if item>smallest_child:
                self.__array[index],self.__array[smallest_child_index]=self.__array[smallest_child_index],self.__array[index]
                self.__check_after_remove(smallest_child_index)
        elif index*2+1<len(self.__array)-1:
            left_child=self.__array[index*2+1]
            if left_child<item:
                self.__array[index],self.__array[index*2+1]=self.__array[index*2+1],self.__array[index]
                self.__check_after_remove(index*2+1)

    def __check_after_insert(self,index):
        parent_index=int((index-1)/2)
        item=self.__array[index]
        parent=self.__array[parent_index]
        if parent>item:
            self.__array[index],self.__array[parent_index]=self.__array[parent_index],self.__array[index]
            self.__check_after_insert(parent_index)
    
    def __str__(self):
        return str(self.__array)