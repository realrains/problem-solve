class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # find first common prefix
        first = -1
        for i in range(len(s)):
            if s[i] == t[0]:
                first = i
                break
        
        # when no common charactor
        if first == -1:
            return len(t)
        
        i = first
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j
