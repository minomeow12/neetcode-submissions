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
        

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            #deleting the node
            node.prev.next = node.next
            node.next.prev = node.prev
            #append it at tail
            last = self.tail.prev
            last.next = node
            node.prev = last
            self.tail.prev = node
            node.next = self.tail
            return node.value     
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.get(key)
            node.value = value
            self.lru[key] = value
        else:
            if len(self.lru) == self.capacity:
                #delete lru cache node, which is head
                first = self.head.next
                first.next.prev = self.head
                self.head.next = first.next
                #delete from hashmap
                self.lru.pop(first.key)
            new_node = ListNode(key,value)
            #append to the dll
            last = self.tail.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.tail
            self.tail.prev = new_node
            #append to hashmap
            self.lru[key] = new_node

