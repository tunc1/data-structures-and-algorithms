class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
    
    def hasNext(self):
        return self.next!=None
    
    def has_previous(self):
        return self.previous!=None

class DoublyLinkedList:

    def __init__(self):
        self.__size=0
    
    def add(self,data):
        node=Node(data)
        if self.is_empty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            node.previous=self.__tail
            self.__tail=node
        self.__size+=1
    
    def add_multiple(self,*items):
        for item in items:
            self.add(item)
    
    def add_to_index(self,item,index):
        if index==0:
            if self.is_empty():
                self.add(item)
            else:
                node=Node(item)
                node.next=self.__head
                self.__head.previous=node
                self.__head=node
                self.__size+=1
        elif index>=self.__size:
            self.add(item)
        else:
            tmp=self.__get_node(index-1)
            node=Node(item)
            tmp.next.previous=node
            node.previous=tmp
            node.next=tmp.next
            tmp.next=node
            self.__size+=1
    
    def get(self,index):
        return self.__get_node(index).data

    def __get_node(self,index):
        if index<(self.__size/2):
            tmp=self.__head
            i=0
            while i<index:
                tmp=tmp.next
                i+=1
        else:
            tmp=self.__tail
            i=self.__size-1
            while i>index:
                tmp=tmp.previous
                i-=1
        return tmp

    def is_empty(self):
        return self.__size==0
    
    def get_last(self):
        return self.__tail.data
    
    def get_first(self):
        return self.__head.data
    
    def remove(self,index):
        if index==0:
            self.__head=self.__head.next
            self.__head.previous=None
        else:
            tmp=self.__get_node(index)
            tmp.previous.next=tmp.next
            tmp.next.previous=tmp.previous
        self.__size-=1
    
    def remove_last(self):
        tmp=self.__get_node(self.__size-2)
        self.__tail=tmp
        tmp.next=None
        self.__size-=1
    
    def pop(self):
        tmp=self.get_last()
        self.remove_last()
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
            while tmp.hasNext():
                tmp=tmp.next
                string+=","+str(tmp.data)
        return "["+string+"]"