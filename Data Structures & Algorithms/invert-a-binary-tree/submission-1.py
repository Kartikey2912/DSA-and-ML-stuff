# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(n):
            if not n:
                return
            n.left, n.right = n.right, n.left
            solve(n.left)
            solve(n.right)
        
        solve(root)
        return root
            