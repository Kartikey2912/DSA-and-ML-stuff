"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}

        def dfs(n):
            if n in mp:
                return mp[n]
            
            cpy = Node(n.val)
            mp[n] = cpy

            for i in n.neighbors:
                cpy.neighbors.append(dfs(i))
            return cpy
        return dfs(node) if node else None