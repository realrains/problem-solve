class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1

        if i == j:
            return 1

        while True:
            if s[i] == s[j]:
                while i + 1 < j and s[i+1] == s[j]:
                    i += 1
                while j - 1 > i and s[j-1] == s[i]:
                    j -= 1
                if j - i > 2:
                    i += 1
                    j -= 1
                else:
                    return j - i - 1
            else:
                return j - i + 1