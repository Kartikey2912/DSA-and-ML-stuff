class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            l,r = i+1, len(nums) - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    ans.append((nums[i], nums[l], nums[r]))
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    l += 1
        return list(set(ans))