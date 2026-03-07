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
14            elif nums[i] + nums[j] > target:
15                j -= 1
16            else:
17                i += 1
18
19        
20
21    def threeSum(self, nums: list[int]) -> list[list[int]]:
22        self.res = []
23
24        nums.sort()
25
26        for i in range(len(nums)):
27            if i > 0 and nums[i] == nums[i-1]:
28                continue 
29            self.two_sum(nums, i+1, -nums[i])
30        
31        return sorted(self.res)
32        