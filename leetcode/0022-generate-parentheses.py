class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def gen(l, r, s):
            if len(s) == n*2:
                result.append(s)
                return
            
            if l < n:
                gen(l+1, r, s + '(')
            
            if r < l:
                gen(l, r+1, s + ')')
        
        gen(0, 0, '')

        return result