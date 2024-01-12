class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        b = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = len(s)
        for i in range(length):
            if i < length // 2 and s[i] in vowels:
                a += 1
            if i >= length // 2 and s[i] in vowels:
                b += 1
        return a == b
