from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2,y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                adj[i].append([d, j])
                adj[j].append([d, i])
        
        ans = 0
        vis = set()
        minH = [[0,0]]
        while len(vis) < n:
            c, node = heappop(minH)
            if node in vis:
                continue
            ans += c
            vis.add(node)
            for neic, nei in adj[node]:
                if nei not in vis:
                    heappush(minH, [neic, nei])
        return ans