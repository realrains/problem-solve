class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = dict()
        d = dict()
        for i, j in zip(s, t):
            if i not in m:
                m[i] = j
            elif i in m and m[i] != j:
                return False

            if j not in d:
                d[j] = i
            elif j in d and d[j] != i:
                return False
        
        return True
