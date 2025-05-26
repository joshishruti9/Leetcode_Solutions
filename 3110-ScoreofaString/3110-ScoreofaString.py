# Last updated: 5/25/2025, 7:46:15 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            total += abs(ord(s[i+1]) - ord(s[i]))
        
        return total
        