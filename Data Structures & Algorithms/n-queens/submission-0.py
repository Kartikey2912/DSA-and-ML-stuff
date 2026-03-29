class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, posDiag, negDiag = set(), set(), set()

        ans = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                ans.append(["".join(i) for i in board])
                return
            for i in range(n):
                if i in col or (r+i) in posDiag or (r-i) in negDiag:
                    continue
                
                col.add(i)
                posDiag.add(r+i)
                negDiag.add(r-i)
                board[r][i] = "Q"

                dfs(r+1)

                col.remove(i)
                posDiag.remove(r+i)
                negDiag.remove(r-i)
                board[r][i] = "."
        dfs(0)
        return ans