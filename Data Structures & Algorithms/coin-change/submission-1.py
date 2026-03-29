class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            res = float("inf")
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1+solve(amount-c))
            dp[amount] = res
            return dp[amount]
        
        ans = solve(amount)
        return ans if ans != float("inf") else -1
            