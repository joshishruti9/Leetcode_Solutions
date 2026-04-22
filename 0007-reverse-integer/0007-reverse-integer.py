class Solution:
    def reverse(self, x: int) -> int:

        mul = -1 if x < 0 else 1

        x = abs(x)

        num = 0
        while x > 0:
            num = (num * 10) + (x % 10)
            x = x // 10

            if num > (2**31)-1 or num < -(2**31):
                return 0
        
        num = num * mul
        
        return num