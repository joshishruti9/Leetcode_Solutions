# Last updated: 4/19/2025, 4:09:40 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        p2 = n-1
       
        while s[p2] == " ":
            p2 -= 1

        i = p2
        p2 += 1
        res = []

        while i > 0:
            if s[i-1] == " ":
                if s[i:p2] != "":
                    res.append(s[i:p2])
                i -= 1
                p2 = i
            else:
                i -= 1

        if s[i:p2] != "":
            res.append(s[i:p2])
        return " ".join(res)