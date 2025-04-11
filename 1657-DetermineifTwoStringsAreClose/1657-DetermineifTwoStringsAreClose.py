# Last updated: 4/10/2025, 10:26:15 PM
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hmap1 = Counter(word1)
        hmap2 = Counter(word2)
        
        if hmap1.keys() != hmap2.keys():
            return False
            
        return Counter(hmap1.values()) == Counter(hmap2.values())