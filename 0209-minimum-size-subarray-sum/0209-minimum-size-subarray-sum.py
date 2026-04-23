class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        p1 = 0
        p2 = 0

        total = 0
        min_len = float("inf")

        while p2 < len(nums):
 
            if total >= target:
                min_len = min(min_len, p2-p1)
                total -= nums[p1]
                p1 += 1
            else:
                total += nums[p2]
                p2 += 1
                
        
        if p2 == len(nums):
            while p1 <= p2 and total >= target:
                total -= nums[p1]
                min_len = min(min_len, p2-p1)
                p1 += 1
            
        return 0 if min_len == float("inf") else min_len
        