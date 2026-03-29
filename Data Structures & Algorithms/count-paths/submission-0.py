class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vis = {}
        def dfs(i, j):
            if i == (m-1) and j == (n-1):
                return 1
            if i >= m or j >= n:
                return 0
            if (i,j) in vis:
                return vis[(i,j)]
            
            vis[(i,j)] = dfs(i+1,j) + dfs(i, j+1)
            return vis[(i, j)]
        return dfs(0, 0)
