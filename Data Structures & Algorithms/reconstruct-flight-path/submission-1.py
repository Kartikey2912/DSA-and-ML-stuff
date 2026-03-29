class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s,d in sorted(tickets)[::-1]:
            adj[s].append(d)
        
        ans = []
        def dfs(s):
            while adj[s]:
                d = adj[s].pop()
                dfs(d)
            ans.append(s)
        
        dfs('JFK')
        return ans[::-1]