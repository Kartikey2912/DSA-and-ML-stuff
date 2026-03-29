class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def solve(i, cur, total):
            if total == target:
                ans.add(tuple(cur))
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            solve(i+1, cur, total + candidates[i])
            cur.pop()
            solve(i+1, cur, total)
        solve(0,[], 0)
        return [list(i) for i in ans]
        