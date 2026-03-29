class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 0
        st = []

        for i,h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                ind, hei = st.pop()
                maxi = max(maxi, hei * (i - ind))
                start = ind
            st.append((start, h))
        
        for i,h in st:
            maxi = max(maxi, h * (len(heights) - i))
        return maxi
