class Node:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def insert(self, data):
        if self.data>data:
            if self.left==None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        if self.data<data:
            if self.right==None:
                self.right=Node(data)
            else:
                self.right.insert(data)

class BinarySearchTree:
    
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.root.insert(data)
    
    def search(self,item):
        tmp=self.root
        while tmp!=None:
            if tmp.data<item:
                tmp=tmp.right
            elif tmp.data>item:
                tmp=tmp.left
            else:
                return True
        return False