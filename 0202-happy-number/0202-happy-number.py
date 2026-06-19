class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n==7:
            return True
        
        if n <= 9:
            return False
        
        num = 0
        while n > 0:
            num += (n % 10) ** 2
            n = n // 10

        return self.isHappy(num)