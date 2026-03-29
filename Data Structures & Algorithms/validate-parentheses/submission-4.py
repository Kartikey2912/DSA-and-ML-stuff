class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if len(st) == 0:
                st.append(i)
            elif i == "(" or i =="[" or i == "{":
                st.append(i)
            elif i == ")" and st[-1] == "(":
                st.pop()
            elif i == "]" and st[-1] == "[":
                st.pop()
            elif i == "}" and st[-1] == "{":
                st.pop()
            else:
                st.append(i)
        return len(st) == 0