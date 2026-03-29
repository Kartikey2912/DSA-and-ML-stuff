class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        row,col = len(grid), len(grid[0])
        vis = set()
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or (r,c) in vis or grid[r][c] != 1:
                return 0
            
            vis.add((r,c))
            res = 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            return res
        
        for r in range(row):
            for c in range(col):
                if (r,c) not in vis and grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        return ans