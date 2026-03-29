class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, c, arr):
            if c == target:
                ans.append(arr.copy())
                return
            
            if i == len(nums) or c > target:
                return
            
            arr.append(nums[i])
            dfs(i, c+nums[i], arr)
            arr.pop()
            dfs(i+1, c, arr)
        dfs(0, 0, [])
        return ans