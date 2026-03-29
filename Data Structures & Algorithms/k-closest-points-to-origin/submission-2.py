from heapq import heappop, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        minH = []
        for p in points:
            x,y = p
            heappush(minH, ((x**2 + y**2) ** 0.5, (x,y)))
        
        while k > 0:
            dis, point = heappop(minH)
            ans.append(point)
            k -= 1
        return ans