class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        curr = n

        while curr != 1:
            if curr in history:
                return False
            history.add(curr)
            curr = sum([int(c)**2 for c in str(curr)])
        
        return True
