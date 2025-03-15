class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        res = []

        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1
        
        word = word1 if p1 < len(word1) else word2
        i = p1 if p1 < len(word1) else p2

        while i < len(word):
            res.append(word[i])
            i += 1

        return "".join(res)
        