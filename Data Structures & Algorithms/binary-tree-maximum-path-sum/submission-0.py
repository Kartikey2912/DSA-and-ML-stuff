# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def dfs(n):
            nonlocal ans
            if not n:
                return 
            left = solve(n.left)
            right = solve(n.right)
            ans = max(ans, n.val+left+right)
            dfs(n.left)
            dfs(n.right)
        
        def solve(n):
            if not n:
                return 0
            left = solve(n.left)
            right = solve(n.right)
            pathsum = n.val + max(left, right)
            return max(0, pathsum)
        dfs(root)
        return ans