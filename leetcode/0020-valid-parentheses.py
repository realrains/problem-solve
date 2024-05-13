class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pair = {'(': ')', '{': '}', '[': ']'}
        for p in s:
            if p in ['(', '{', '[']:
                stk.append(p)
            elif stk and pair[stk[-1]] == p:
                stk.pop()
            else:
                return False
        
        return len(stk) == 0
