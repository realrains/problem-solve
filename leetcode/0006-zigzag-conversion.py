class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]

        currRow = 0
        delta = 1
        i = 0
        while i < len(s):
            rows[currRow].append(s[i]) 
            
            i += 1

            if delta > 0 and currRow == numRows - 1:
                delta = -1
            elif delta < 0 and currRow == 0:
                delta = 1

            currRow += delta
        
        return ''.join([''.join(row) for row in rows])
