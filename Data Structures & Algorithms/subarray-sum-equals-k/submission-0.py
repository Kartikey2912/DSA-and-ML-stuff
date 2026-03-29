class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0
        mp = {0: 1}

        for i in nums:
            curr += i
            diff = curr - k

            ans += mp.get(diff, 0)
            mp[curr] = 1 + mp.get(curr, 0)
        return ans