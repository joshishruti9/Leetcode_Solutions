1class Solution:
2    def two_sum(self, nums, start, target):
3
4        i = start
5        j = len(nums)-1
6
7        while i < j:
8            if nums[i] + nums[j] == target:
9                self.res.append([-target, nums[i], nums[j]])
10                i += 1
11                j -= 1
12                while i < j and nums[i] == nums[i-1]:
13                    i += 1
14                
15                while i < j and nums[j] == nums[j+1]:
16                    j -= 1
17
18            elif nums[i] + nums[j] > target:
19                j -= 1
20            else:
21                i += 1
22
23        
24
25    def threeSum(self, nums: list[int]) -> list[list[int]]:
26        self.res = []
27
28        nums.sort()
29
30        for i in range(len(nums)):
31            if i > 0 and nums[i] == nums[i-1]:
32                continue 
33            self.two_sum(nums, i+1, -nums[i])
34        
35        return sorted(self.res)
36        