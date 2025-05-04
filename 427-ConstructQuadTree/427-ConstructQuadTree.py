# Last updated: 5/4/2025, 4:07:26 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        i = n-1

        if digits[i] != 9:
            digits[i] = digits[i] + 1
            return digits
        
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        
        if i < 0:
            digits = [1] + [0 for j in range(n)]
        else:
            digits[i] = digits[i] + 1

        return digits
        