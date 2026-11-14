# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        s = dummy
        r = dummy
        i = 0
        while i < n + 1:
            r = r.next
            i += 1
        while r is not None:
            r = r.next
            s = s.next
        s.next = s.next.next
        return dummy.next
        