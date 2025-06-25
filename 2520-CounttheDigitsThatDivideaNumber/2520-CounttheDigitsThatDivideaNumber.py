# Last updated: 6/25/2025, 3:12:50 PM
class Solution:
    def countDigits(self, num: int) -> int:

        digits = []

        n = num

        while n > 0:
            digits.append(n % 10)
            n = n // 10

        print(digits)
        count = 0
        for digit in digits:
            if num % digit == 0:
                count += 1
        
        return count