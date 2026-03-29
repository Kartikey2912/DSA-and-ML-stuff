class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        mp = defaultdict(list)
        for i in range(n):
            key = [0] * 26
            for j in range(len(strs[i])):
                ind = ord(strs[i][j]) - ord('a')
                key[ind] += 1
            mp[tuple(key)].append(strs[i])
        return list(mp.values())