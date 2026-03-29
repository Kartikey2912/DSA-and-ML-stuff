"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None:None}
        curr = head
        while curr:
            c = Node(curr.val)
            mp[curr] = c
            curr = curr.next
        curr = head
        while curr:
            c = mp[curr]
            c.next = mp[curr.next]
            c.random = mp[curr.random]
            curr = curr.next
        return mp[head]