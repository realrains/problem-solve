class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        mapping = {}
        r_mapping = {}
        for word, p in zip(words, pattern): 
            if p in mapping and mapping[p] != word:
                return False
            if word in r_mapping and r_mapping[word] != p:
                return False
            mapping[p] = word
            r_mapping[word] = p
        
        return True
