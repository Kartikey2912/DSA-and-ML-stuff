from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for i in stones:
            heappush(arr, -i)
        while len(arr) > 1:
            i = -heappop(arr)
            j = -heappop(arr)
            if i == j:
                continue
            else:
                val = abs(i - j)
                heappush(arr, -val)
        return -arr[0] if len(arr) == 1 else 0 
