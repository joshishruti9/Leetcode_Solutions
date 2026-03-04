1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n = len(height)
4
5        i = 0
6        j = n-1
7
8        max_area = 0
9
10        while i < j:
11            area = (j-i) * min(height[i],height[j])
12
13            max_area = max(max_area, area)
14
15            if height[i] < height[j]:
16                i += 1
17            else:
18                j -= 1
19        
20        return max_area
21        