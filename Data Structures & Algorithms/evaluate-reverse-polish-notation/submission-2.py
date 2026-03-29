class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i == "+":
                a = int(st.pop())
                b = int(st.pop())
                st.append(a+b)
            elif i == "-":
                a = int(st.pop())
                b = int(st.pop())
                st.append(b-a)
            elif i == "*":
                a = int(st.pop())
                b = int(st.pop())
                st.append(b*a)
            elif i == "/":
                a = int(st.pop())
                b = int(st.pop())
                st.append(b/a)
            else:
                st.append(i)
            print(st[0])
        return int(st[0])
                