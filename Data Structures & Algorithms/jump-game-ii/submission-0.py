class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l,r = 0, 0

        while r < len(nums) - 1:
            maxi = 0
            for i in range(l, r+1):
                maxi = max(maxi, i + nums[i])
            l = r+1
            r = maxi
            ans += 1
        return ans