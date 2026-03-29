class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            pr = prices[i]-prices[i-1]
            if pr > 0:
                ans += pr
        return ans