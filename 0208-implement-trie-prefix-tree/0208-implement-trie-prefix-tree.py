class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        node = self.trie

        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        
        node["end"] = True


    def search(self, word: str) -> bool:
        node = self.trie

        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        
        return True if "end" in node else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)