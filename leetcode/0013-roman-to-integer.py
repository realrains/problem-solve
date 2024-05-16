class Solution:
    def romanToInt(self, s: str) -> int:
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = float('inf')
        for c in s:
            if v[c] > prev:
                result += v[c]
                result -= 2 * prev
            else:
                result += v[c]
            prev = v[c]
        return result
