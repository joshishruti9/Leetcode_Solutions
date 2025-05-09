# Last updated: 5/8/2025, 7:29:54 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n*(n+1)) // 2
        add = 0

        for i in range(n):
            add += nums[i]
        
        return total-add