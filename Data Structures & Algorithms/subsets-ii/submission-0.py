class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        def dfs(i, arr):
            if i == len(nums):
                ans.add(tuple(arr))
                return
            ans.add(tuple(arr))
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
            dfs(i+1, arr)
        dfs(0, [])
        return [list(i) for i in ans]