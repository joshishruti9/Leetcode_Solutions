1class Solution:
2    def countVowelSubstrings(self, word: str) -> int:
3    
4        '''
5        i = 0
6        j = 0 
7        max_len = 0
8        count_map = {}
9        res = 0
10
11        while j < len(word):
12            if word[j] not in vowels:
13                while i < j:
14                    if word[i] in count_map:
15                        count_map[word[i]] -= 1
16                        if count_map[word[i]] == 0:
17                            del count_map[word[i]]
18                        
19                        if len(count_map) == 5:
20                            res += 1
21                    i += 1
22                
23                i = j
24                j += 1
25                count_map.clear()
26                continue
27            else:
28                count_map[word[j]] = count_map.get(word[j],0) + 1
29                if len(count_map) == 5:
30                    res += 1
31                
32                j += 1
33        '''
34
35        vowels = set('aeiou')
36        n = len(word)
37        count_map = {}
38        res = 0
39
40        for i in range(n):
41            if word[i] not in vowels:
42                continue
43
44            count_map[word[i]] = count_map.get(word[i], 0) + 1 
45            for j in range(i+1,n):
46                if word[j] in vowels:
47                    count_map[word[j]] = count_map.get(word[j], 0) + 1
48                    if len(count_map) == 5:
49                        res += 1
50                else:
51                    break            
52            count_map = {}
53        
54        return res
55
56
57
58