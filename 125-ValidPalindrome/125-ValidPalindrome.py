# Last updated: 5/28/2025, 7:36:00 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() == s[p2].lower():
                    p1 += 1
                    p2 -= 1
                else:
                    return False
            elif s[p1].isalnum():
                p2 -= 1
            else:
                p1 += 1
        return True

        