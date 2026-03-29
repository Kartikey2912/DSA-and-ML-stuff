class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        p = self.permute(nums[1:])
        ans = []
        for i in p:
            for j in range(len(i)+1):
                c = i.copy()
                c.insert(j, nums[0])
                ans.append(c)
        return ans