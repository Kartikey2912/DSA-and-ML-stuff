class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        if sum(nums) % 2:
            return False
        
        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if (i,target) in dp:
                return dp[(i, target)]
            
            dp[(i, target)] = dfs(i+1, target) or dfs(i+1, target - nums[i])
            return dp[(i, target)]
        return dfs(0, sum(nums)//2)
        