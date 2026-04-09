class Solution:
    def is_palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i+1:j]       

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest_str = ""
        for i in range(len(s)):
            
            odd = self.is_palindrome(s, i, i)
            even = self.is_palindrome(s, i, i + 1)
            
            if len(odd) > len(longest_str):
                longest_str = odd
            if len(even) > len(longest_str):
                longest_str = even
                
        return longest_str

        