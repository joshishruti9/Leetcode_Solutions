# Last updated: 8/5/2025, 4:41:09 PM
class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current_trie = self.trie

        for letter in word:
            if letter not in current_trie:
                current_trie[letter] = {}
            current_trie = current_trie[letter]
        current_trie['End'] = True
        
    def traverse(self, word, index, current_trie):

        if index == len(word):
            return "End" in current_trie

        letter = word[index]

        if letter is ".":
            for char in current_trie:
                if char is "End":
                    continue
                #current_trie = current_trie[char]
                if self.traverse(word, index + 1, current_trie[char]):
                    return True
            return False

        elif letter not in current_trie:
            return False

        else:
            current_trie = current_trie[letter]
            return self.traverse(word, index + 1, current_trie)

    def search(self, word: str) -> bool:
        current_trie = self.trie

        flag = self.traverse(word, 0, current_trie)
        return flag


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)