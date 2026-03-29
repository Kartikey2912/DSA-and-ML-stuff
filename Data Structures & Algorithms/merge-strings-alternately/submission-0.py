class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0, 0
        cnt = 0
        ans = ""
        while i < len(word1) and j < len(word2):
            if cnt % 2 == 0:
                ans += word1[i]
                i += 1
                cnt += 1
            else:
                ans += word2[j]
                j += 1
                cnt += 1
        while i < len(word1):
            ans += word1[i]
            i += 1
        while j < len(word2):
            ans += word2[j]
            j += 1
        return ans