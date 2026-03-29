class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = False
        i = 0
        n = len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans