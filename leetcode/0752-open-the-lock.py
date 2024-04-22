from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pending = deque()
        pending.append((0, '0000'))
        curr = '0000'
        visited = {de: True for de in deadends}

        if curr in visited:
            return -1

        while pending:
            depth, curr = pending.popleft()

            if curr == target:
                return depth

            for i in range(4):
                nxt = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i+1:]
                prv = curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i+1:]

                if nxt not in visited:
                    pending.append((depth+1, nxt))
                    visited[nxt] = True
                
                if prv not in visited:
                    pending.append((depth+1, prv))
                    visited[prv] = True
                
        return -1
