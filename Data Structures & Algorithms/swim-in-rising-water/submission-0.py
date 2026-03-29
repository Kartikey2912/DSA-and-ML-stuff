from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = set()
        minH = [[grid[0][0], 0, 0]]
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        vis.add((0,0))
        while minH:
            t,r,c = heappop(minH)
            if r == n-1 and c == n-1:
                return t
            for dr,dc in direc:
                neir, neic = r+dr, c+dc
                if (neir < 0 or neic < 0 or neir >= n or neic >= n or (neir, neic) in vis):
                    continue
                vis.add((neir, neic))
                heappush(minH, [max(t, grid[neir][neic]), neir, neic])
        return -1