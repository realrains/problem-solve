class Solution:
    def mySqrt(self, x: int) -> int:
        for r in range(x + 1):
            if r * r > x:
                return r - 1
        return x
