class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, cp):
            if i >= len(nums):
                ans.append(cp.copy())
                return 
            cp.append(nums[i])
            dfs(i+1, cp)
            cp.pop()
            dfs(i+1, cp)
        dfs(0, [])
        return ans
            