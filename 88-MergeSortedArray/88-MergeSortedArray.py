# Last updated: 6/30/2025, 9:55:59 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        
        index = i if i > 0 else j
        nums = nums1 if i > 0 else nums2

        while index >= 0:
            nums1[k] = nums[index]
            index -= 1
            k -= 1        