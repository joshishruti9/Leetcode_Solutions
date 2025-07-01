# Last updated: 6/30/2025, 9:57:11 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[0:n] = nums2

        ptr1_tail = m - 1
        ptr2_tail = n - 1
        ptr = m + n - 1

        while ptr1_tail >= 0 and ptr2_tail >= 0:
            if nums1[ptr1_tail] > nums2[ptr2_tail]:
                nums1[ptr] = nums1[ptr1_tail]
                ptr1_tail -= 1
            else:
                nums1[ptr] = nums2[ptr2_tail]
                ptr2_tail -= 1
            ptr -= 1
            
        
        while ptr2_tail >= 0:
            nums1[ptr] = nums2[ptr2_tail]
            ptr2_tail -= 1
            ptr -= 1

