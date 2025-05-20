# Last updated: 5/20/2025, 12:26:39 AM
class Solution:
    def merge(self, left, right):
        i = 0
        j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result += left[i:]
        result += right[j:]

        return result
    
    def merge_sort(self, nums, low, high):
        if low == high:
            return nums[low:high+1]
        
        mid = (low + high) // 2

        left = self.merge_sort(nums,low,mid)
        right = self.merge_sort(nums,mid+1,high)

        return self.merge(left,right)

    def sortArray(self, nums: List[int]) -> List[int]:

        return self.merge_sort(nums,0,len(nums)-1)