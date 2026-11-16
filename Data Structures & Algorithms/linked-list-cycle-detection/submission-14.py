# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        if head is None:
            return False
            
        if head.next is None:
            return False
        

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        #time: O(n)
        #space: O(1)

    #s = 1
    #f = 1
    #1st: 

        