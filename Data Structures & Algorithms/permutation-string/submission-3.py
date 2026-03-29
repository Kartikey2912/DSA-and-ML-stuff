class Solution:
    def count(self, s):
        mp = [0] * 26
        for i in s:
            mp[ord(i) - ord("a")] += 1
        return mp
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)-1
        mp1 = [0] * 26
        for i in s1:
            mp1[ord(i) - ord("a")] += 1
        while r < len(s2):
            s = s2[l:r+1]
            m = self.count(s)
            if m == mp1:
                return True
            else:
                l += 1
                r += 1
        return False
            
    