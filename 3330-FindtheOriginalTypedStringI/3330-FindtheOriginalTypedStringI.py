# Last updated: 8/7/2025, 5:16:33 PM
from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        n = len(word)-1
        for i in range(n):
            if word[i] == word[i+1]:
                count += 1
            
        return count+1