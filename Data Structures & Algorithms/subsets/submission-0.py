class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def solve(i):
            if i >= len(nums):
                ans.append(sub.copy())
                return
            
            sub.append(nums[i])
            solve(i+1)
            sub.pop()
            solve(i+1)
        solve(0)
        return ans