class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_cnt = s.count('1')
        return ('1' * (one_cnt - 1)) + '0' * (len(s) - one_cnt) + '1'