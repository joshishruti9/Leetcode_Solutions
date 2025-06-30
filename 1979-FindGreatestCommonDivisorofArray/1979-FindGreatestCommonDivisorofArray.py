# Last updated: 6/30/2025, 4:37:16 PM
class Solution:
    def find_min(self, nums):
        min_num = float('inf')

        for num in nums:
            min_num = min(min_num, num)
        
        return min_num
    
    def find_max(self,nums):
        max_num = float('-inf')

        for num in nums:
            max_num = max(max_num, num)
        
        return max_num
    
    def find_gcd(self, num1, num2):

        if num1 == 0 :
            return num2
        elif num2 == 0:
            return num1

        num = self.find_gcd(num2, num1 % num2)
        
        return num

    def findGCD(self, nums: List[int]) -> int:
        min_num = self.find_min(nums)
        max_num = self.find_max(nums)

        gcd_num = self.find_gcd(max_num, min_num)

        return gcd_num