class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]


    def insert(self, key: int, value: int) -> None:

        #check if key already exist in table
        index = hash(key) % self.capacity
        for i in range(len(self.table[index])):
            k,v = self.table[index][i]
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        #append
        
        #check if needing to resize
        if (self.size+1) / self.capacity >= 0.5:
            self.resize()
            index = hash(key) % self.capacity
        self.table[index].append((key, value))
        self.size += 1
        





    def get(self, key: int) -> int:
        #get the bucket
        index = hash(key) % self.capacity
        #search in the bucket
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1 

    def remove(self, key: int) -> bool:
        index = hash(key) % self.capacity
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.size -= 1
                return True
        return False
            



    def getSize(self) -> int:
        return self.size
        


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for bucket in self.table:
            for key,value in bucket:
                index = hash(key) % new_capacity
                new_table[index].append((key, value))
        self.table = new_table
        self.capacity = new_capacity

