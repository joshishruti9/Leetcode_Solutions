# Last updated: 5/24/2025, 7:39:34 PM
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        counter = Counter(nums)
        total = 0
        for val in counter.values():
            total += (val * (val-1)) // 2
        
        return total
        