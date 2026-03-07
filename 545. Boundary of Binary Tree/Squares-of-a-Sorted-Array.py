1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3
4        i = 0
5        j = len(nums)-1
6        res = [0 for i in range(len(nums))]
7        k = j
8
9        while i <= j:
10            if abs(nums[i]) <= abs(nums[j]):
11                res[k] = abs(nums[j]) ** 2
12                j -= 1
13                k -= 1
14            
15            else:
16                res[k] = abs(nums[i]) ** 2
17                i += 1
18                k -= 1
19        
20        return res
21
22
23        