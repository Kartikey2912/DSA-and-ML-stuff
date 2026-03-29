class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        vis = set()
        row,col = len(grid), len(grid[0])
        ans = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= col or (r,c) in vis or grid[r][c] == 0:
                return 0
            vis.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(row):
            for c in range(col):
                if (r,c) not in vis and grid[r][c] == 1:
                    ans = max(ans,dfs(r,c))
        return ans 
        