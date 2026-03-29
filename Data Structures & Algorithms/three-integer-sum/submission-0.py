class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return ([])
        
        triplets = []
        nums = sorted(nums)
        
        for i in range(0, len(nums)-2):
            
            lower = i+1
            upper = len(nums)-1
            
            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                
                if s==0:
                    triplets.append((nums[i], nums[lower], nums[upper]))
                    lower += 1
                elif s<0:
                    lower += 1
                else:
                    upper -= 1
        
        return(list(set(triplets)))
        
                