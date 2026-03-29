class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1), len(s2)
        if n > m:
            return False
        mp = [0] * 26
        for i in range(n):
            mp[ord(s1[i]) - ord("a")] += 1
        l,r = 0, n-1
        while r < m:
            mp1 = [0] * 26
            for i in range(l,r+1):
                mp1[ord(s2[i]) - ord("a")] += 1
            if mp1 == mp:
                return True
            l += 1
            r += 1
        return False
            
            