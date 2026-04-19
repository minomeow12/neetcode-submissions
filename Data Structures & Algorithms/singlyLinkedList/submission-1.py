class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        count = 0
        current = self.head
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1
            
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        if not self.tail:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index-1 and current:
            i += 1
            current = current.next
        if not current.next:
            return False
        else:
            current.next = current.next.next
            return True


    def getValues(self) -> List[int]:
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next
        return arr
        
