# Last updated: 4/10/2025, 1:14:46 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        for num in nums1:
            if num in set2:
                set1.remove(num)
                set2.remove(num)
        
        return [list(set1), list(set2)]