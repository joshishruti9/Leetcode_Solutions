class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0

        i = 0
        while i < len(nums):
            if lsum == rsum - nums[i]:
                return i
            lsum += nums[i]
            rsum -= nums[i]
            i += 1
        return -1