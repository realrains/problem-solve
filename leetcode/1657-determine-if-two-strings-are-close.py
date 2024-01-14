class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = dict(), dict()
        
        for c in word1:
            if c in cnt1:
                cnt1[c] += 1
            else:
                cnt1[c] = 1
        
        for c in word2:
            if c in cnt2:
                cnt2[c] += 1
            else:
                cnt2[c] = 1
        
        return set(cnt1) == set(cnt2) and sorted(list(cnt1.values())) == sorted(list(cnt2.values()))
