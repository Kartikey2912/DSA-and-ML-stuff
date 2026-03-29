# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solve(n, m):
            if not n and not m:
                return True
            if n and m and n.val == m.val:
                return solve(n.left, m.left) and solve(n.right, m.right)
            else:
                return False
        return solve(p, q)