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
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        i = 0
        curr = self.head
        while i < index - 1 and curr:
            i += 1
            curr = curr.next
        
        if not curr or not curr.next:
            return False
            
        if not curr.next.next:

            curr.next = None
            self.tail = curr
            return True
        else:
            curr.next = curr.next.next
            return True
     


    def getValues(self) -> List[int]:
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next
        return arr
        
