# Last updated: 5/28/2025, 7:31:52 PM
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
            
        for i in range(n):
            num = (3 ** i)
            print(num)
            if n == num:
                return True
            elif num > n:
                break
        
        return False
