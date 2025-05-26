# Last updated: 5/25/2025, 7:58:16 PM
class Solution:
    def convertDateToBinary(self, date: str) -> str:

        i = 0
        res = []
        n = len(date)
        num = 0

        while i < n:
            if date[i] != '-':
                num = num * 10 + int(date[i]) 
            else:
                date_num = bin(num)[2:]
                res.append(date_num)
                res.append('-')
                num = 0
            i += 1

        date_num = bin(num)[2:]
        res.append(date_num)
        return "".join(res)    