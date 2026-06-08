class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:

        curr_node = self.trie

        for char in word:
            if char in curr_node:
                curr_node = curr_node[char]
            else:
                curr_node[char] = {}
                curr_node = curr_node[char]

        curr_node["end"] = True 
    

    def traverse(self, word, index, curr_node):
        if index == len(word):
            return "end" in curr_node

        letter = word[index]

        if letter == ".":
            for char in curr_node:

                if char is "end":
                    continue
                
                if self.traverse(word, index + 1, curr_node[char]):
                    return True
            return False

        elif letter not in curr_node:
            return False

        else:
            curr_node = curr_node[letter]
            return self.traverse(word, index + 1, curr_node)   

    def search(self, word: str) -> bool:

        curr_node = self.trie

        return self.traverse(word, 0, curr_node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)