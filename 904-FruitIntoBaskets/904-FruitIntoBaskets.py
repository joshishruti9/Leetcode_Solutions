# Last updated: 8/20/2025, 8:34:58 PM
from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        i = 0
        j = 0
        count = 0
        max_len = 0
        hmap = {}
        last_index = i
    
        while j < len(fruits):
            if fruits[j] not in hmap:
                if len(hmap) == 2:
                    max_len = max(max_len, j-i)
                    min_index = min(hmap.values())
                    hmap.pop(fruits[min_index])
                    i = min_index + 1
            hmap[fruits[j]] = j
            j += 1
  
        max_len = max(max_len, j-i)   
        return max_len
        