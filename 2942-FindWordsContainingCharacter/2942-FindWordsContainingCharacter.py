# Last updated: 5/24/2025, 7:41:55 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
            
        return res