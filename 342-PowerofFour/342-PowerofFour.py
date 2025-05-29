# Last updated: 5/28/2025, 7:24:23 PM
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False
            
        log_val = math.log(n, 4)        
        return int(log_val) == log_val

        '''for i in range(n//2):
            num = (4 ** i)
            if n == num:
                return True
            elif num > n:
                break
        
        return False'''