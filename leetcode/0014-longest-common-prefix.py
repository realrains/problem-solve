class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i, cc in enumerate(zip(strs[0], strs[-1])):
            if cc[0] != cc[1]:
                return strs[0][:i]
        return strs[0]
