class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        i = n-1

        count = 0
        flag = True

        while i >= 0:
            if s[i] == " " and flag:
                i -= 1
            elif s[i] == " " and not flag:
                break
            elif s[i].isalnum():
                count += 1
                i -= 1
                flag = False
        
        return count