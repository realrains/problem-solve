class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bitcounter = [0] * 22

        for n in nums:
            binary = str(bin(n))[2:][::-1]
            for i in range(len(binary)):
                if binary[i] == '1':
                    bitcounter[i] += 1
        
        for i in range(len(bitcounter)):
            bitcounter[i] %= 2
        
        bk = str(bin(k))[2:][::-1]

        for i in range(len(bk)):
            bitcounter[i] = abs(bitcounter[i] - int(bk[i]))

        return sum(bitcounter)
