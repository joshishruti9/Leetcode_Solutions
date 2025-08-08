# Last updated: 8/7/2025, 5:15:32 PM
from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                count += 1
            
        return count+1