class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        simplified = []

        for part in parts:
            if part == '..':
                if simplified:
                    simplified.pop()
            elif part == '.' or part == '':
                continue
            else:
                simplified.append(part)
        
        return '/' + '/'.join(simplified)
