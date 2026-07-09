class Solution:
    def sumAndMultiply(self, n: int) -> int:

        total = 0
        num = 0
        count = 0

        while n > 0:
            last_num = n % 10
            if last_num != 0:
                total += last_num
                num = (last_num * (10 ** count)) + num
                count += 1
            
            n = n // 10
        
        return num * total
        