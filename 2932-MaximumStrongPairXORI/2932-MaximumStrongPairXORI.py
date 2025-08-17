# Last updated: 8/16/2025, 8:58:03 PM
from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        i = j = 0
        count = 0
        max_count = 0
        queue = deque()

        while j < len(nums):
            if nums[j] == 0:
                if count == k:
                    max_count = max(max_count, j-i)
                    if queue:
                        i = (queue.popleft()) + 1
                        count -= 1
                    else:
                        i += 1
                        j = i
                        count = count - 1
                        print("Count:", count)
                        count = max(count,0)
                    
                    print("max_count: ",max_count,"j: ",j, "i: ",i)
                else:
                    count += 1
                    queue.append(j)
                    j += 1
            else:
                j += 1
        
        max_count = max(max_count, j-i)
        return max_count