# Last updated: 5/27/2025, 1:57:34 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = []
        right_sum = [0 for i in range(n)]
        total = 0

        for i in range(n):
            left_sum.append(total)
            total += nums[i]
        
        total = 0
        for i in range(n-1,-1,-1):
            right_sum[i] = total
            total += nums[i]
        
        for i in range(n):
            left_sum[i] = abs(left_sum[i] - right_sum[i])
        
        return left_sum