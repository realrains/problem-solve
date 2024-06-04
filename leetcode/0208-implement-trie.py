class Trie:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['leaf'] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return 'leaf' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return True
