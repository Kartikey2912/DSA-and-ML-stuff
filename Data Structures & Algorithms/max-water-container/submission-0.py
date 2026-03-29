class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l,r = 0, len(heights) - 1
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = height * base
            ans = max(area, ans)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return ans