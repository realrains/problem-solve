class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in reversed(s):
            if c != ' ':
                count += 1
            elif count > 0 and c == ' ':
                break
        return count
