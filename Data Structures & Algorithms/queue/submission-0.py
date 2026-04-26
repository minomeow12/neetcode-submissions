
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left


    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False
        
        

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        if self.isEmpty():
            self.left.next = new_node
            new_node.prev = self.left
            self.right.prev = new_node
            new_node.next = self.right
        else:
            last = self.right.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.right
            self.right.prev = new_node
            

        

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.append(value)
        else:
            new_node = ListNode(value)
            first = self.left.next
            new_node.prev = self.left
            self.left.next = new_node
            new_node.next = first
            first.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.right.prev
        value = last.val
        if last == self.left.next:
            self.left.next = self.right
            self.right.prev = self.left
            return value
        last.prev.next = self.right
        self.right.prev = last.prev
        return value
   

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.left.next
        value = first.val
        if first == self.right.prev:
            return self.pop()
        self.left.next = first.next
        first.next.prev = self.left
        return value
      
        
