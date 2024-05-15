class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""
        for c1, c2 in zip(strs[0], strs[-1]):
            if c1 != c2:
                return prefix
            else:
                prefix += c1
        
        return prefix
