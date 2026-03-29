class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        vis = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in vis:
                return vis[(i, j)]
            
            if text1[i] == text2[j]:
                vis[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                vis[(i,j)] = max(dfs(i+1,j), dfs(i,j+1))
            return vis[(i,j)]
        
        return dfs(0, 0)