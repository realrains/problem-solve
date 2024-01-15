class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = dict(), dict()

        for w, l in matches:
            if w not in win:
                win[w] = 1
                lose[w] = 0
            else:
                win[w] += 1
            
            if l not in lose:
                lose[l] = 1
                win[l] = 0
            else:
                lose[l] += 1
        
        return [
            sorted([k for k, v in lose.items() if v == 0]),
            sorted([k for k, v in lose.items() if v == 1]),
            ]
        