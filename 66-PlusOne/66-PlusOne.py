# Last updated: 4/26/2025, 3:21:20 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = 0
        num = 0 

        for i in range(len(digits)):
            num = (num * 10) + digits[i]
        
        return [int(digit) for digit in str(num+1)]