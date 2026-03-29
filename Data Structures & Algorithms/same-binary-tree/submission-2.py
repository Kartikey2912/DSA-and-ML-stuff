# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(l,r):
            if not l and not r:
                return True
            if not l:
                return False
            if not r:
                return False
            if l.val != r.val:
                return False
            ans = solve(l.left, r.left) and solve(l.right, r.right)
            return ans
        return solve(p, q)