class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # mp = Counter(nums)
        # ans = []
        # n = len(nums)
        # for i,v in mp.items():
        #     if v > math.floor(n // 3):
        #         ans.append(i)
        # return ans
        mp = defaultdict(int)
        ans = set()
        n = len(nums)
        for i in nums:
            mp[i] = 1 + mp.get(i, 0)
            if mp[i] > math.floor(n//3):
                ans.add(i)
            if len(ans) == 2:
                return list(ans)
        return list(ans)