class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i == "+":
                v1 = int(st.pop())
                v2 = int(st.pop())
                st.append(v2 + v1)
            elif i == "-": 
                v1 = int(st.pop())
                v2 = int(st.pop())
                st.append(v2 - v1) 
            elif i == "*":
                v1 = int(st.pop())
                v2 = int(st.pop())
                st.append(v2 * v1)
            elif i == "/":
                v1 = int(st.pop())
                v2 = int(st.pop())
                st.append(v2 / v1)
            else:
                st.append(i)
            print(st)
        return int(st[0])
            