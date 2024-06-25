class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        n = len(digits)
        codes = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if n == 0:
            return result

        def dfs(combination, depth):
            if depth == n:
                result.append(combination)
                return
            
            for c in codes[digits[depth]]:
                dfs(combination + c, depth + 1)
        
        dfs('', 0)
        return result
