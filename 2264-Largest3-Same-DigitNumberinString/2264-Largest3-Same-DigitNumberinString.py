# Last updated: 6/25/2025, 10:42:24 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        i = 0
        max_val = ""

        while i < len(num)-2:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                max_val = max(max_val, num[i]) 
            i += 1
        return  max_val*3 if max_val else ""