class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []

        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        word = word1 if i < len(word1) else word2

        while i < len(word):
            res.append(word[i])
            i += 1

        return "".join(res)
        