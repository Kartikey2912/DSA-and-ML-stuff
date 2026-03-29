class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n,m = len(s), len(t)
        if n != m:
            return False
        mp, mp1 = defaultdict(int), defaultdict(int)
        for i in range(n):
            mp[s[i]] += 1
            mp1[t[i]] += 1
        
        for i, v in mp.items():
            if mp1[i] != v:
                return False
        return True