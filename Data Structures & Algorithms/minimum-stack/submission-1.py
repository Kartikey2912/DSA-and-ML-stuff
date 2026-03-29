class MinStack:

    def __init__(self):
        self.st = []
        self.mini = float("inf")
    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(0)
            self.mini = val
        else:
            self.st.append(val - self.mini)
            if val < self.mini:
                self.mini = val
    def pop(self) -> None:
        if not self.st:
            return
        val = self.st.pop()
        if val < 0:
            self.mini = self.mini - val
    def top(self) -> int:
        ans = self.st[-1]
        if ans <= 0:
            return self.mini
        else:
            return ans + self.mini

    def getMin(self) -> int:
        return self.mini
