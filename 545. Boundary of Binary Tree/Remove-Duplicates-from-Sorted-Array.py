1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3
4        k = 1
5
6        for i in range(1, len(nums)):
7            if nums[i] != nums[i-1]:
8                nums[k] = nums[i]
9                k += 1
10        
11        return k
12        