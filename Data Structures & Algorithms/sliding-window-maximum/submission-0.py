class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j = 0, k-1
        ans = []
        while j < len(nums):
            arr = nums[i:j+1]
            maxi = max(arr)
            ans.append(maxi)
            i += 1
            j += 1
        return ans