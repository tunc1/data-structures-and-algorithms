class Stack():
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__array=[]
    
    def push(self,item):
        if len(self.__array)<self.__max_size:
            self.__array.append(item)
            self.__max_size+=1
    
    def pop(self):
        tmp=self.__array[-1]
        del self.__array[-1]
        return tmp
    
    def top(self):
        return self.__array[-1]

    def size(self):
        return len(self.__array)
    
    def is_empty(self):
        return self.size()==0