class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin,curmax = 1, 1
        ans = nums[0]

        for i in nums:
            temp = curmax * i
            curmax = max(curmax*i, curmin*i, i)
            curmin = min(temp, curmin*i, i)

            ans = max(ans, curmax)
        return ans