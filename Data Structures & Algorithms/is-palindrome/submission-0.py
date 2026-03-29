class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i,j = 0, n - 1

        while i <= j:
            v,w = s[i].lower(), s[j].lower()
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if v != w:
                return False
            i += 1
            j -= 1
        return True