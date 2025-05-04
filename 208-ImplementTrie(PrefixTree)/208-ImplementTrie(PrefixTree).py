# Last updated: 5/3/2025, 5:47:11 PM
class Trie:

    def __init__(self):
       self.trie = {} 

    def insert(self, word: str) -> None:
        current_trie = self.trie
        for character in word:
            if character not in current_trie:
                current_trie[character] = {}
            current_trie = current_trie[character]
        current_trie['isEnd'] = True
            

    def search(self, word: str) -> bool:
        current_trie = self.trie

        for character in word:
            if character not in current_trie:
                return False

            current_trie = current_trie[character]
        
        return 'isEnd' in current_trie
        

    def startsWith(self, prefix: str) -> bool:
        current_trie = self.trie
        flag = False
        for character in prefix:
            if character not in current_trie:
                return False
            current_trie = current_trie[character]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)