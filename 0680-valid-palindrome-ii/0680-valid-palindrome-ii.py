class Solution:
    def check_palindrome(self, s, i, j, count):

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif count == 0:
                count += 1
                return self.check_palindrome(s, i+1, j, count) or self.check_palindrome(s, i, j-1, count)
            else:
                return False
        
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.check_palindrome(s, 0, len(s)-1,0)
        

        