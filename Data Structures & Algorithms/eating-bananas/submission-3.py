class Solution:
    def solve(self, n, piles, h):
        cnt = 0
        for i in piles:
            cnt += math.ceil(i / n)
        return [cnt <= h,cnt]

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l+r)//2
            res, cnt = self.solve(mid, piles, h)
            if res:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans 
            
