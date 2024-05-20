class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid_row(row):
            count = [0] * 9
            for i in board[row]:
                if not i.isdigit():
                    continue
                n = int(i)
                if count[n-1] != 0:
                    return False
                count[n-1] += 1
            return True
        
        def is_valid_col(col):
            count = [0] * 9
            for row in range(9):
                i = board[row][col]
                if not i.isdigit():
                    continue
                n = int(i)
                if count[n-1] != 0:
                    return False
                count[n-1] += 1
            return True
        
        def is_valid_box(row, col):
            count = [0] * 9
            for x in range(3):
                for y in range(3):
                    i = board[row*3+y][col*3+x]
                    if not i.isdigit():
                        continue
                    n = int(i)
                    if count[n-1] != 0:
                        return False
                    count[n-1] += 1
            return True
        
        for i in range(9):
            if not is_valid_row(i):
                return False
            if not is_valid_col(i):
                return False
        
        for a, b in ((x, y) for x in range(3) for y in range(3)):
            if not is_valid_box(a, b):
                return False
        
        return True
