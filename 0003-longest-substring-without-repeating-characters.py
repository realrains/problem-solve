class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        ans = 0
        d = dict()
        start = 0

        for end in range(N):
            if s[end] in d:
                start = max(d[s[end]], start)
            
            ans = max(ans, end - start + 1)
            d[s[end]] = end + 1
        
        return ans

