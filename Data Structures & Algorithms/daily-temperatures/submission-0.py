class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = [] 

        for i, v in enumerate(temperatures):
            while st and v > st[-1][0]:
                val, ind = st.pop()
                ans[ind] = i - ind
            st.append([v, i])
        return ans