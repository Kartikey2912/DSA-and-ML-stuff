# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {v:i for i,v in enumerate(inorder)}
        i = 0
        def build(l,r):
            nonlocal i
            if l > r:
                return None
            val = preorder[i]
            i += 1
            middle_ind = mp[val]
            root = TreeNode(val)
            root.left = build(l, middle_ind-1)
            root.right = build(middle_ind+1, r)
            return root
        return build(0, len(inorder) - 1)