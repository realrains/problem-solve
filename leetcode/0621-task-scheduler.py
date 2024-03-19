class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters = [0 for _ in range(ord('Z') - ord('A') + 1)]
        
        max_cnt = -1

        for task in tasks:
            i = ord(task) - ord('A')
            letters[i] += 1
            max_cnt = max(max_cnt, letters[i])
        
        additions = 0

        for letter in letters:
            if max_cnt == letter:
                additions += 1
        
        return max((max_cnt - 1) * (n + 1) + additions, len(tasks))
