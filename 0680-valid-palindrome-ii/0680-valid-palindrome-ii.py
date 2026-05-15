class Solution:
    def check_palindrome(self, s, i, j):

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                return self.check_palindrome(s, start+1, end) or self.check_palindrome(s, start, end-1)
            start += 1
            end -= 1
        
        return True
        

        