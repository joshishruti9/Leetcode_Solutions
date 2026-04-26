class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1 or n == 7:
            return True
        
        if n <= 9:
            return False
        
        total = 0
        while n > 0:
            total += ((n % 10) * (n % 10))
            n = n // 10
        
        return self.isHappy(total)