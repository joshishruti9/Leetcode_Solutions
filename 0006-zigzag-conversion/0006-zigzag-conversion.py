from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        row_map = defaultdict(list)
        i = 0
        k = 0

        while i < len(s):
            k = 0
            while i < len(s) and k < numRows:
                row_map[k].append(s[i])
                k += 1
                i += 1
            
            k -= 2
            while i < len(s) and k > 0:
                row_map[k].append(s[i])
                i += 1
                k -= 1
        
        res = ""
        for i in range(numRows): 
            res += ("".join(row_map[i]))

        return res