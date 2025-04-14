# Last updated: 4/13/2025, 10:32:41 PM
class Solution:
    def reverse_num(self,num):
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = (rev_num * 10) + digit
            num = num // 10
        
        return rev_num
        
    def isPalindrome(self, x: int) -> bool:
        rev_num = self.reverse_num(abs(x))
        return x == rev_num 
        