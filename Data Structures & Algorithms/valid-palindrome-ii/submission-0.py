class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)  
        l,r = 0, n-1 
        while l < r:
            if s[l] != s[r]:
                ls = s[l+1:r+1]
                rs = s[l:r]
                return ls == ls[::-1] or rs == rs[::-1]
            l += 1
            r -= 1
        return True