class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        str1, str2 = strs[0], strs[-1]
        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] != str2[i]:
                return str1[:i]
            i += 1
        return str1[:i]
        
