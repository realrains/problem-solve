class Solution:
    def __init__(self):
        self.dp = [[None for _ in range(101)] for _ in range(101)]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if self.dp[len(s1)][len(s2)] is not None:
            return self.dp[len(s1)][len(s2)]
        if len(s3) == 0 and len(s1) == 0 and len(s2) == 0:
            return True
        if len(s3) == 0 and (len(s1) > 0 or len(s2) > 0):
            return False

        result = False

        if s1 and s3[0] == s1[0]:
            result = result or self.isInterleave(s1[1:], s2, s3[1:])
        if s2 and s3[0] == s2[0]:
            result = result or self.isInterleave(s1, s2[1:], s3[1:])
        
        self.dp[len(s1)][len(s2)] = result
        return result
