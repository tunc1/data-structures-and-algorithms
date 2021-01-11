from linked_list import LinkedList

class Queue():
    def __init__(self):
        self.__list=LinkedList()
    
    def enqueue(self,item):
        self.__list.add(item)
    
    def dequeue(self):
        return self.__list.pop()

    def peek(self):
        return self.__list.get_first()
    
    def __str__(self):
        return str(self.__list)