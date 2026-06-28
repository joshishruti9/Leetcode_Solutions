class Solution:
    def romanToInt(self, s: str) -> int:

        symbol_num_dict = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M":1000}

        res = symbol_num_dict[s[len(s)-1]]
        i = len(s)-2

        while i >= 0:
            if symbol_num_dict[s[i]] < symbol_num_dict[s[i+1]]:
                res -= symbol_num_dict[s[i]]
                i -= 1
            else:
                res += symbol_num_dict[s[i]]
                i -= 1
        
        return res



        