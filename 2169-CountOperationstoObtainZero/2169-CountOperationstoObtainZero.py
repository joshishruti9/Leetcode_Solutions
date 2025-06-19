# Last updated: 6/18/2025, 9:29:01 PM
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        if num1 == 0 or num2 == 0:
            return 0
        
        if num1 == num2:
            return 1
        
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            
            count += 1
        
        return count