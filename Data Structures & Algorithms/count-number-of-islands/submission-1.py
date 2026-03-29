class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        row, col = len(grid), len(grid[0])
        vis = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or (r,c) in vis or grid[r][c] != "1":
                return
            vis.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in vis:
                    dfs(r,c)
                    ans += 1
        return ans