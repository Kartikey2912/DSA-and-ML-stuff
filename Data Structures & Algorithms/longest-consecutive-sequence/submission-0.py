class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vis = set(nums)
        ans = 0
        for i in vis:
            if (i - 1) not in vis:
                l = 1
                while i + l in vis:
                    l += 1
                ans = max(ans, l)
        return ans