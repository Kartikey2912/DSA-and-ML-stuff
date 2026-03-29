class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking in columns
        for row in range(9):
            vis = set()
            for i in range(9):
                val = board[row][i]
                if val == ".":
                    continue
                if val in vis:
                    return False
                vis.add(val)
        #checking in rows
        for col in range(9):
            vis = set()
            for i in range(9):
                val = board[i][col]
                if val == ".":
                    continue
                if val in vis:
                    return False
                vis.add(val)
        
        #checking in boxes
        for sq in range(9):
            vis = set()
            for i in range(3):
                for j in range(3):
                    r = (sq // 3) * 3 + i
                    c = (sq % 3) * 3 + j
                    val = board[r][c]
                    if val == ".":
                        continue
                    if val in vis:
                        return False
                    vis.add(val)
        return True



