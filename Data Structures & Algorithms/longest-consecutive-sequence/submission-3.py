class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in mp:
                l = 1
                while i+1 in mp:
                    l += 1
                    i += 1
                ans = max(ans, l)
        return ans

