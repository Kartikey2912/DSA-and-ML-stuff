class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def dfs(i, c, arr):
            if c == target:
                ans.add(tuple(arr))
                return
            
            if i == len(candidates) or c > target:
                return
            
            arr.append(candidates[i])
            dfs(i+1, c+candidates[i], arr)
            arr.pop()
            dfs(i+1, c, arr)
        dfs(0,0,[])
        return [list(arr) for arr in ans]
            