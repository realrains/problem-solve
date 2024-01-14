class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scnt = [0 for _ in range(26)]
        tcnt = [0 for _ in range(26)]

        for sc, tc in zip(s, t):
            scnt[ord(sc) - 97] += 1
            tcnt[ord(tc) - 97] += 1
        
        return sum([abs(x - y) for x, y in zip(scnt, tcnt)]) // 2
