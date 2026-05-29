class Solution:
    
    # take 2 pointers start and end
    # increment end and add nums[end] till total < target
    # if total == target find min_len
    # else total > target substarct start value from total and increment start
    #Once end reaches at end == len(nums), substarct start value from total and increment start and check min_len at each step if total == target
    # return min_len

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        end = 0
        start = 0
        total = 0
        min_len = float("inf")

        while end < len(nums):
            if total < target:
                total += nums[end]
                end += 1
            
            if total >= target:
                min_len = min(min_len, end-start)
                total -= nums[start]
                start += 1

        if end == len(nums):
            while total >= target:
                min_len = min(min_len, end-start)
                total -= nums[start]
                start += 1
            
        
        return min_len if min_len != float("inf") else 0
            
