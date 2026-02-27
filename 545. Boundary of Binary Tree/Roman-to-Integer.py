1class Solution:
2    def romanToInt(self, s: str) -> int:
3
4        hmap = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM":900, "M":1000}
5
6
7        i = 0
8        res = 0
9        while i < len(s)-1:
10            if s[i:i+2] in hmap:
11                res += hmap[s[i:i+2]]
12                i += 2
13            else:
14                res += hmap[s[i:i+1]]
15                i += 1
16        
17        if i == len(s)-1:
18            res += hmap[s[i]]
19        
20        return res