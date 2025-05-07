# Last updated: 5/7/2025, 12:41:46 PM
from collections import Counter

def sort_func(item):
    return item[1]

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        sorted_list = sorted(counter.items(), key = sort_func, reverse = True)

        return [item[0] for item in sorted_list[:k]]