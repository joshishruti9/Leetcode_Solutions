# Last updated: 5/28/2025, 7:16:51 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        for i in range(n//2):
            num = (4 ** i)
            if n == num:
                return True
            elif num > n:
                break
        
        return False
        