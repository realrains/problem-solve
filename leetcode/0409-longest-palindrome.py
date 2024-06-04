class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        odd = 0

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        result = 0
        for c in letters:
            if letters[c] % 2 == 1:
                odd = 1
                result += letters[c] - 1
            if letters[c] % 2 == 0:
                result += letters[c]
        
        return result + odd
