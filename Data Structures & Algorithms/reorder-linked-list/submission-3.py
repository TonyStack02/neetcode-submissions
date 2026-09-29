# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head

        #mesuring the length
        while curr:
            length += 1
            curr = curr.next

        #splitting the list in 2 half
        curr = head
        prev = None

        compenser = 0
        if length % 2!= 0:
            compenser += 1
        for i in range ((length + compenser)// 2):
            prev = curr
            curr = curr.next
        
        head2 = curr
        prev.next = None #detaching the 1st half by the 2nd 

        #reversing the 2nd half
        curr = head2
        prev = None 
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        #merging
        first = head
        current = head

        counter = 0
        while head and head2:
            
            if counter % 2 == 0:
                head = head.next
                current.next = head2
                current = head2
            else:
                head2 = head2.next
                current.next = head
                current = head
            counter += 1




