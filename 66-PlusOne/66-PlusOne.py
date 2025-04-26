# Last updated: 4/26/2025, 3:36:42 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        i = n - 1

        if digits[i] != 9:
            digits[n-1] = digits[n-1] + 1
            return digits
        
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        
        if i >= 0:
            digits[i] = digits[i] + 1
        else:
            digits = [1] + [0 for i in range(n)]

        return digits