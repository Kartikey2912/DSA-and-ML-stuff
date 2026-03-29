class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []
        for i,v in enumerate(temperatures):
            while st and st[-1][0] < v:
                val, j = st.pop()
                ans[j] = i - j 
            st.append([v, i])
        return ans