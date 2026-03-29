from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxhe = [[float("inf"),-100001]]
        mp = Counter(nums)
        for i,v in mp.items():
            heappush(maxhe, [-1*v, i])
        ans = []
        for i in range(k):
            cnt, val = heappop(maxhe)
            ans.append(val)
        return ans