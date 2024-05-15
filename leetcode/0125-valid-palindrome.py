class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ''.join((c for c in s if c.isalpha() or c.isdigit())).lower()
        i, j = 0, len(target) - 1

        while i < j:
            if target[i] != target[j]:
                return False
            i+=1
            j-=1
        
        return True
