class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        min_len = float("inf")
        curr_sum = 0

        while j < len(nums):
            if curr_sum >= target:
                min_len = min(min_len, (j-i))
                curr_sum -= nums[i]
                i += 1
            else:
                curr_sum += nums[j]
                j += 1
        
        if j == len(nums):
            while i < j and curr_sum >= target:
                min_len = min(min_len, (j-i))
                curr_sum -= nums[i]
                i += 1
        
        return min_len if min_len < float("inf") else 0