class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        row, col = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c >= col or r >= row or c < 0 or (r,c) in vis or grid[r][c] == "0":
                return
            vis.add((r, c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        ans = 0
        for i in range(row):
            for j in range(col):
                if (i,j) not in vis and grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        return ans

