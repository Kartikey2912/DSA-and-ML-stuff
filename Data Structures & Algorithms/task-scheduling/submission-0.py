class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for i in tasks:
            cnt[ord(i) - ord("A")] += 1
        
        cnt.sort()
        maxi = cnt[-1]
        idle = (maxi - 1) * n

        for i in range(24, -1,-1):
            idle -= min(maxi - 1, cnt[i])
        
        return max(0, idle) + len(tasks)