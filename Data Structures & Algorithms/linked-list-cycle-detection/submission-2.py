# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        a = head
        b = head
        if a == None:
            return False
        if a.next == None:
            return False
        a = a.next
        b = b.next.next
        while a and b:
            if a is b:
                return True
            a = a.next
            b = b.next
            if b == None:
                return False
            else:
                b= b.next
        
        return False
        