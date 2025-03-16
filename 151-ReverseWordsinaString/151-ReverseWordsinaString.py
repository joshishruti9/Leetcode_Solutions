class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        n = len(s) - 1
        i = n
        
        while s[i] == " ":
            i -= 1

        p2 = i + 1
        p1 = i
        while i >= 0:
            if s[i] == " ":
                if s[i+1] != " ":
                    res.append(s[i+1:p2])
                p2 = i
            i -= 1
        if s[i+1] != ' ':
            res.append(s[i+1:p2])
        return " ".join(res)