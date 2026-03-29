class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        mp, win = defaultdict(int), defaultdict(int)
        for c in t:
            mp[c] += 1
        
        match, confirm = 0, len(mp)
        slice = [-1,-1]
        mini = float("inf")
        l = 0
        for r in range(len(s)):
            win[s[r]] += 1
            if s[r] in mp and win[s[r]] == mp[s[r]]:
                match += 1
            while match == confirm:
                if (r - l + 1) < mini:
                    mini = r - l + 1
                    slice = [l, r]
                win[s[l]] -= 1
                if s[l] in mp and win[s[l]] < mp[s[l]]:
                    match -= 1
                l += 1
        i,j = slice
        return s[i:j+1] if mini != float("inf") else ""
