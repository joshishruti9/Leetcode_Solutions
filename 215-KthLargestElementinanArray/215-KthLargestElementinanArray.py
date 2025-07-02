# Last updated: 7/2/2025, 12:51:39 PM
from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(len(nums)):
            if len(min_heap) < k:
                heappush(min_heap,nums[i])
            else:
                num = heappop(min_heap)
                if nums[i] > num:
                    heappush(min_heap,nums[i])
                else:
                    heappush(min_heap,num)
        
        return heappop(min_heap)

        