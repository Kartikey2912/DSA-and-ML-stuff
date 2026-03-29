# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = []
        q = deque()
        q.append(root)

        while q:
            n = len(q)
            s = []
            for i in range(n):
                child = q.popleft()
                if child:
                    q.append(child.left)
                    q.append(child.right)
                    s.append(child.val)
            if s:
                level.append(s)
        ans = []
        for i in level:
            ans.append(i[-1])
        return ans