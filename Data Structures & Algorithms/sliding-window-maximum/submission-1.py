from heapq import heappop, heappush
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxH = []
        ans = []
        for i in range(len(nums)):
            heappush(maxH, [-nums[i], i])
            if i >= k-1:
                while maxH[0][1] <= i-k:
                    heappop(maxH)
                ans.append(-maxH[0][0])
        return ans
        
        
            
    
