class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        vis = set(wordDict)
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            
            if i in dp:
                return dp[i]
            
            for j in range(i, len(s)):
                if s[i:j+1] in vis:
                    if dfs(j+1):
                        dp[i] = True
                        return dp[i]
            dp[i] = False
            return dp[i]
        return dfs(0)
            