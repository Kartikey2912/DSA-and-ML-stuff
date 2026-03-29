# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {val: ind for ind, val in enumerate(inorder)}

        pre = 0
        def solve(l, r):
            nonlocal pre
            if l > r:
                return None

            val = preorder[pre]
            pre += 1
            root = TreeNode(val)
            mid = mp[val]
            root.left = solve(l, mid-1)
            root.right = solve(mid+1, r)
            return root
        return solve(0, len(inorder) - 1)