# Last updated: 7/2/2025, 12:43:06 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort(reverse=True)
        return nums[k-1]
        