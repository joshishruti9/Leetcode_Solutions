1class Solution:
2    def trap(self, height: List[int]) -> int:
3        #leave all the numbers till you reach some height. After that all the heights in stack and maintain a monotonic stack such as as soon as you get height greater than previous pop everything out and calculate area. (currheight-smallestheight) add that to final area. continue to do that. 
4
5        stack = []
6        n = len(height)
7        area = 0
8
9        i = 0
10        while i < n and height[i] <= 0:
11            i += 1
12        
13        if i == n:
14            return 0
15        
16    
17        curr_high = height[i]
18
19        while i < n:
20            if height[i] <= curr_high:
21                stack.append(height[i])
22                i += 1
23            else:
24                min_val = min(curr_high, height[i])
25                while stack:
26                    num = stack.pop()
27                    area += (min_val - num)
28
29                curr_high = height[i]
30                stack.append(height[i])    
31                i += 1
32        
33        if stack:
34            max_right = stack.pop()
35
36            while stack:
37                val = stack.pop()
38                if val > max_right:
39                    max_right = val
40                else:
41                    area += (max_right - val)            
42
43        
44        return area
45        