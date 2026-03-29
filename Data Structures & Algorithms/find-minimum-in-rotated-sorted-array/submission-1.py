class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l,r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
                ans = min(ans, nums[l])
        return ans
        