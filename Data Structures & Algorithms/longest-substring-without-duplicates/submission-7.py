class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in vis:
                vis.remove(s[l])
                l += 1
            vis.add(s[r])
            ans = max(ans, r-l+1)
        return ans
