class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        s,e = 0, c-1

        while s < r and e >= 0:
            ele = matrix[s][e]
            if ele == target:
                return True
            elif ele > target:
                e -= 1
            else:
                s += 1
        return False
