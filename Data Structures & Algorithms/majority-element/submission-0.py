class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for i,v in c.items():
            if v >= math.floor(n//2):
                return i
            