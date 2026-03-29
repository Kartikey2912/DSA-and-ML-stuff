# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def dfs(n):
            if not n: return 0
            left = max(0,dfs(n.left))
            right = max(0,dfs(n.right))
            ans[0] = max(ans[0], n.val + left + right)
            return n.val + max(left, right)
        dfs(root)
        return ans[0]
