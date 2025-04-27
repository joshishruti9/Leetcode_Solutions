# Last updated: 4/26/2025, 5:00:31 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        res = [0 for i in range(n)]

        j = n-1
        k = n-1

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] * nums[i]
                i += 1
            else:
                res[k] = nums[j] * nums[j]
                j -= 1
            k -= 1

        return res