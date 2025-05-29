# Last updated: 5/29/2025, 4:35:09 PM
class Solution:
    def reverse(self, x: int) -> int:

        mul = 1 if x > 0 else -1

        x = abs(x)
        rev_num = 0

        while x != 0 :
            rev_num = rev_num * (10) + (x%10)
            x = x // 10
        
        rev_num = rev_num * mul

        if rev_num > (2**31)-1 or rev_num < -1 * (2**31):
            return 0
        
        return rev_num