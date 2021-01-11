class HashTable:
    
    def __init__(self,size):
        self.__objects=[]
        self.__keys=[]
        self.__size=size
        for i in range(size):
            self.__objects.append([])
            self.__keys.append(None)
    
    def delete(self,key):
        index=hash(key)%self.__size
        key_values=self.__objects[index]
        if len(key_values)==1:
            del key_values[0]
        else:
            for index,key_value in enumerate(key_values):
                if key_value.key==key:
                    del key_values[index]
    
    def insert(self,key,value):
        index=hash(key)%self.__size
        self.__objects[index].append(KeyValue(key,value))
        self.__keys[index]=key
    
    def get(self,key):
        index=hash(key)%self.__size
        key_values=self.__objects[index]
        if len(key_values)==1:
            return key_values[0].value
        else:
            for key_value in key_values:
                if key_value.key==key:
                    return key_value.value
        return None

class KeyValue:
    
    def __init__(self,key,value):
        self.key=key
        self.value=value