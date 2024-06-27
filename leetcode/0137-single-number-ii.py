class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pos_counter = [0] * 32
        neg_counter = [0] * 32

        for n in nums:
            if n > 0:
                for i, b in enumerate(bin(n)[2:].zfill(32)):
                    pos_counter[i] = (pos_counter[i] + int(b)) % 3
            else:
                for i, b in enumerate(bin(n)[3:].zfill(32)):
                    neg_counter[i] = (neg_counter[i] + int(b)) % 3

        pos = sum([b * (2 ** i) for i, b in enumerate(reversed(pos_counter))])
        neg = -sum([b * (2 ** i) for i, b in enumerate(reversed(neg_counter))])

        return pos + neg
        