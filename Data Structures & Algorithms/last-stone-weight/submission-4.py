from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-i for i in stones]
        heapify(st)
        while len(st) > 1:
            print(st)
            one, two = -heappop(st), -heappop(st)
            if one == two:
                continue
            else:
                heappush(st, -abs(one-two))
        return -st[0] if len(st) == 1 else 0