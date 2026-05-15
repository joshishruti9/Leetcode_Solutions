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

        res.append(word1[i:])
        res.append(word2[j:])
        
        return "".join(res)
        