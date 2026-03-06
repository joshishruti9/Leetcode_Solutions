1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        occured = set()
4        max_len = 0
5        count = 0
6        i = 0
7        j = 0
8
9        while j < len(s):
10            if s[j] not in occured:
11                occured.add(s[j])
12                j += 1
13            else:
14                max_len = max(max_len, j-i)
15                occured.remove(s[i])
16                i += 1
17        
18        max_len = max(max_len, j-i)
19        return max_len