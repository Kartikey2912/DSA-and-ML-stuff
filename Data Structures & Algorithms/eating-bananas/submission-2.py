class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #range = 1 to max(piles)

        lower, upper = 1, max(piles)
        ans = upper
        # def solve(mid):
        #     cnt = 0
        #     for i in piles:
        #         val = i
        #         while val > 0:
        #             val -= mid
        #             cnt += 1
        #     if cnt <= h:
        #         return True
        #     else:
        #         return False
        while lower <= upper:
            mid = (lower+upper)//2
            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            if time <= h:
                ans = mid
                upper = mid - 1
            else:
                lower = mid + 1
        return ans
