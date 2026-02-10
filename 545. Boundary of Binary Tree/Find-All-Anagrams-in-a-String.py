1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3
4        res = []
5
6        hmp = {}
7        hms = {}
8
9        for key in p:
10            hmp[key] = hmp.get(key,0) + 1
11        
12        i = 0
13        j = 0
14        n = len(p)
15
16        while j < len(s):
17 
18            hms[s[j]] = hms.get(s[j], 0) + 1
19
20            if j-i+1 > n:
21                hms[s[i]] = hms[s[i]] - 1
22                if hms[s[i]] == 0:
23                    hms.pop(s[i])
24                i += 1
25            
26            if j-i+1 == n:
27                if hms == hmp:
28                    res.append(i)
29
30            j += 1
31                
32        return res