# Last updated: 7/14/2025, 10:44:30 PM
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        counter = Counter(s)

        def sort_func(key):
            return counter[key]

        ans = sorted(counter, reverse= True, key = sort_func)
        res = []
        for letter in ans:
            val = counter[letter]
            for i in range(val):
                res.append(letter)
        
        return "".join(res)
        