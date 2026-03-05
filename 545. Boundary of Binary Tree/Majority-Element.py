1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3
4        count = 0
5        num = 0
6
7        for i in range(len(nums)):
8            if count == 0:
9                num = nums[i]
10
11            if nums[i] == num:
12                count += 1
13            else:
14                count -= 1
15        
16        return num
17            
18        