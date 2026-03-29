class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        vis = set()

        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            
            for j,v in enumerate(i):
                if v == target[j]:
                    vis.add(j)
        
        return len(vis) == 3