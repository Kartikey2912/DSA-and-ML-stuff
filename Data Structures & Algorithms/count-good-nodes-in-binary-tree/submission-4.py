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
            ans = 0
            if n.val >= maxi:
                ans = 1
            maxi = max(n.val, maxi)
            ans += solve(n.left, maxi) 
            ans += solve(n.right, maxi)
            return ans
        return solve(root, root.val)
        