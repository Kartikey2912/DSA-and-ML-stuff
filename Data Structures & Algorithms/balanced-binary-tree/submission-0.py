# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def solve(n):
            if not n:
                return [True, 0]
            
            left = solve(n.left)
            right = solve(n.right)

            ans = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [ans, 1 + max(left[1], right[1])]
        ans = solve(root)
        return ans[0]