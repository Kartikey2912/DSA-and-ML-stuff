# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def solve(n, maxi):
            if not n:
                return 0
            res = 0
            if n.val >= maxi:
                res = 1
            maxi = max(maxi, n.val)
            res += solve(n.left, maxi)
            res += solve(n.right, maxi)
            return res
        
        return solve(root, root.val)