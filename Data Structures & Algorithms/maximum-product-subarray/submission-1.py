class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxi, curr = 1, 1

        for i in nums:
            temp = i * maxi
            maxi = max(temp, i * curr, i)
            curr = min(temp, i * curr, i)
            ans = max(ans, maxi)
        return ans