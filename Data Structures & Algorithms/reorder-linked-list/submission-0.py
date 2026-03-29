# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head.next
        #split in two
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        s.next = None
        prev = None
        next = second
        #reverse the second
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        #merge the two
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
        