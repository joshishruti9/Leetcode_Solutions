1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3
4        res = 0 
5
6        for num in nums:
7            res = res ^ num
8        
9        return res
10
11