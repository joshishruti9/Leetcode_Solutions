# Last updated: 6/25/2025, 10:41:03 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        i = 0
        max_val = "0"

        while i < len(num)-2:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                s = num[i:i+3]
                if int(s[0]) >= int(max_val[0]):
                    max_val = num[i:i+3]
                i += 3  
            else:
                i += 1

        return  max_val if len(max_val) >= 3 else ""