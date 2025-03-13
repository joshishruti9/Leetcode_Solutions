class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 9:
            if n == 1 or n == 7:
                return True
            else:
                return False 

        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        return self.isHappy(total)