class Solution:
    def romanToInt(self, s: str) -> int:

        symbol_num_dict = {"I" : 1, "IV" : 4, "V" : 5, "IX" : 9, "X":10, "XL":40, "L":50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M":1000}

        res = 0
        i = 0

        while i < len(s)-1:
            if s[i:i+2] in symbol_num_dict:
                res += symbol_num_dict[s[i:i+2]]
                i += 2
            else:
                res += symbol_num_dict[s[i]]
                i += 1
        
        if i == len(s)-1:
            res += symbol_num_dict[s[i]]

        return res



        