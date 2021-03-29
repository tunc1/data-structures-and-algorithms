class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def hasNext(self):
        return self.next!=None

class CircularLinkedList():
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def add(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            self.__tail=node
            self.__tail.next=self.__head
        self.__size+=1

    def add_multiple(self,*items):
        for item in items:
            self.add(item)
    
    def add_to_index(self,item,index):
        if index==0:
            node=Node(item)
            node.next=self.__head
            self.__head=node
            self.__size+=1
            self.__tail.next=self.__head
        elif index>=self.__size:
            self.add(item)
        else:
            tmp=self.__head
            i=0
            while i<index-1:
                tmp=tmp.next
                i+=1
            node=Node(item)
            node.next=tmp.next
            tmp.next=node
            self.__size+=1

    def get(self,index):
        tmp=self.__head
        i=0
        while i<index:
            tmp=tmp.next
            i+=1
        return tmp.data
    
    def get_last(self):
        return self.get(self.__size-1)

    def get_first(self):
        return self.get(0)
    
    def remove(self,index):
        if index==0:
            self.__head=self.__head.next
            self.__tail.next=self.__head
        else:
            tmp=self.__head
            i=0
            while i<index-1:
                tmp=tmp.next
                i+=1
            tmp.next=tmp.next.next
        self.__size-=1
    
    def remove_last(self):
        self.remove(self.get_size()-1)
    
    def pop(self):
        tmp=self.get_last()
        self.remove(self.__size-1)
        return tmp
    
    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size==0
    
    def __str__(self):
        string=""
        if not self.is_empty():
            tmp=self.__head
            string+=str(tmp.data)
            while tmp.hasNext() and tmp.next!=self.__head:
                tmp=tmp.next
                string+=","+str(tmp.data)
        return "["+string+"]"