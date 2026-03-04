1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3
4        res = []
5        j = 0
6
7        if len(strs) == 1:
8            return strs[0]
9
10        while True:
11            for i in range(len(strs) - 1):
12                if (j >= len(strs[i]) or j >= len(strs[i+1])  or strs[i][j] != strs[i+1][j]):
13                    return "".join(res)
14            
15            res.append(strs[i][j])
16            j += 1
17    
18        return "".join(res)        