class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)
        ans = []
        n = len(nums)
        for i,v in mp.items():
            if v > math.floor(n // 3):
                ans.append(i)
        return ans