1class Solution:
2    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
3        n = len(word)
4        res = True
5
6        j = 0
7        i = 0
8        num = 0
9
10        while j < n and i < len(abbr):
11            if 'a' <= abbr[i] <= 'z':
12                if j < n :
13                    res = res and abbr[i] == word[j]
14                i += 1
15                j += 1
16            else:
17                if abbr[i] == '0':
18                    return False
19
20                num = 0
21                while i < len(abbr) and '0' <= abbr[i] <= '9':
22                    num = num * 10 + int(abbr[i])
23                    i += 1
24                
25                j += num
26        
27        return res and j == n and i == len(abbr)
28
29
30        