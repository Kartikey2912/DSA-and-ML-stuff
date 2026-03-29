class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # cur, maxi = 0, nums[0]
        # for i in nums:
        #     if cur < 0:
        #         cur = 0
        #     cur += i
        #     maxi = max(maxi, cur)
        # return maxi
        ans = nums[0]
        maxi = nums[0]
        for i in range(1, len(nums)):
            maxi = max(maxi+nums[i], nums[i])
            ans = max(maxi, ans)
        return ans