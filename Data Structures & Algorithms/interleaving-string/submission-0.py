class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o = len(s1), len(s2), len(s3)
        dp = {}
        if n + m != o:
            return False
        
        def dfs(i,j,k):
            if k == o:
                return (i == n) and (j == m)
            
            if (i, j) in dp:
                return dp[(i, j)]
            ans = False
            if i < n and s1[i] == s3[k]:
                ans = dfs(i+1, j, k+1)
            if not ans and j < m and s2[j] == s3[k]:
                ans = dfs(i, j+1, k+1)
            dp[(i, j)]=ans
            return dp[(i, j)]
        return dfs(0, 0, 0)