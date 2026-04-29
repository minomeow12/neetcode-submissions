class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    #helper func
    #remove first
    def remove_lru(self):
            #delete node
            first = self.head.next
            first.next.prev = self.head
            self.head.next = first.next
            #delete in hashmap
            self.lru.pop(first.key)


    #insert at tail
    def insert(self, node):
            last = self.tail.prev
            last.next = node
            node.prev = last
            self.tail.prev = node
            node.next = self.tail

    #remove the node
    def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev



        

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            #deleting the node
            self.remove(node)
            #append it at tail
            self.insert(node)
            return node.value     
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            
        else:
            if len(self.lru) == self.capacity:
                #remove lru
                self.remove_lru()       
            new_node = ListNode(key,value)
            #append to the dll
            self.insert(new_node)
            #append to hashmap
            self.lru[key] = new_node

