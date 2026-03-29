class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        arr = []
        def ispali(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i):
            if i >= len(s):
                ans.append(arr.copy())
                return
            
            for j in range(i, len(s)):
                if ispali(i,j):
                    arr.append(s[i:j+1])
                    dfs(j+1)
                    arr.pop()
        dfs(0)
        return ans