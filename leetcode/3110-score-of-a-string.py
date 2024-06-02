class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = ord(s[0])

        for c in s[1:]:
            i = ord(c)
            score += abs(i - prev)
            prev = i
        
        return score
