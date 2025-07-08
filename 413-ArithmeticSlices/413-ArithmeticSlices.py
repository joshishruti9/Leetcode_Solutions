# Last updated: 7/7/2025, 7:18:32 PM
class Solution:
    def find_count(self, num):
        return (num - 2) * (num - 1) // 2
        
    def find_subarrays(self, nums):

        n = len(nums)
        i = 0
        total = 0
        
        while i < n-2:
            diff = nums[i+1] - nums[i]
            j = i + 1
            while j + 1 < n and nums[j + 1] - nums[j] == diff:
                j += 1

            
            total += self.find_count(j-i+1)
            i = j       
    
        return total

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        self.dp = dict()
        self.dp[3] = 1
        self.dp[2] = 0 
        self.dp[1] = 0   
        total = self.find_subarrays(nums)
        return total 