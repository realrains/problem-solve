class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        result = 0
        
        for token in tokens:
            try:
                stk.append(int(token))
                continue
            except:
                pass
            
            rhs = stk.pop()
            lhs = stk.pop()

            if token == '+':
                stk.append(lhs + rhs)
            elif token == '-':
                stk.append(lhs - rhs)
            elif token == '*':
                stk.append(lhs * rhs)
            elif token == '/':
                stk.append(int(lhs / rhs))
        
        return stk.pop()
