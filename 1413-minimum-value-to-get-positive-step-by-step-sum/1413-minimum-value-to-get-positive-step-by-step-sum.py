class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        total = 0
        min_total = float("inf")

        for num in nums:
            total += num
            min_total = min(total, min_total)
        
        return max(1, 1 - min_total)

        