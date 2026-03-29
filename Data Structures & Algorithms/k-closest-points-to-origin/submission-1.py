from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
    
        def dist(arr: List[int])->int:
            x1,y1 = arr[0], arr[1]
            dis = (x1 * x1 + y1 * y1) ** 0.5
            return dis
        
        for i in points:
            dis = dist(i)
            heappush(minH, [dis, i])
        ans = []
        for i in range(k):
            dis, coor = heappop(minH)
            ans.append(coor)
        return ans
            