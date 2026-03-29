# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solve(n):
            nonlocal ans
            if not n:
                return 0
            left = solve(n.left)
            right = solve(n.right)
            ans = max(ans, left + right)
            return 1 + max(left, right)
        solve(root)
        return ans