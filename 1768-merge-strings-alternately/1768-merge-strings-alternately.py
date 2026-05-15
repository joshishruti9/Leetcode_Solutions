class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i = 0
        j = 0

        word1_len = len(word1)
        word2_len = len(word2)
        res = []

        while i < word1_len and j < word2_len:
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1
        
        if i == word1_len:
            while j < word2_len:
                res.append(word2[j])
                j += 1
        
        if j == word2_len:
            while i < word1_len:
                res.append(word1[i])
                i += 1
        
        return "".join(res)
        