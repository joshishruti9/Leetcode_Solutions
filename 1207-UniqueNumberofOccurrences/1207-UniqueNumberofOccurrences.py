# Last updated: 4/10/2025, 12:49:47 PM
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurrence = set()
        
        for key, value in counter.items():
            if value in occurrence:
                return False
            else:
                occurrence.add(value)
        
        return True