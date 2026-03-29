class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(perm, nums, pick):
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        pick = [False] * len(nums)
        dfs([], nums, pick)
        return ans