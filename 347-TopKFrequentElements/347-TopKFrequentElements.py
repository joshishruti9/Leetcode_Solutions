# Last updated: 5/7/2025, 1:16:57 PM
from heapq import heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        min_heap = []

        for key, value in counter.items():
            if len(min_heap) < k:
                heappush(min_heap,(value,key))
            else:
                v, keys = heappop(min_heap)
                if value > v:
                    heappush(min_heap,(value,key))
                else:
                    heappush(min_heap,(v,keys))

        return [item[1] for item in min_heap]   