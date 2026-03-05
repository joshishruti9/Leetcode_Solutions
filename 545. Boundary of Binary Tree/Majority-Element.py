1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3
4        num_counter = Counter(nums)
5        n = len(nums)
6
7        for key, val in num_counter.items():
8            if val > (n//2):
9                return key
10        