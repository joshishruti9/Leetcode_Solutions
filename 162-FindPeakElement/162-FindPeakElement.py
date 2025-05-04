# Last updated: 5/4/2025, 1:48:22 PM
class Solution:
    def bisect_left(self, nums, low, high):

        print(low," ",high)

        if low == high:
            self.peak = high
            return
      
        mid = (low + high) // 2
        
        if mid == 0 and nums[mid+1] < nums[mid]:
            print("con2")
            self.peak = mid
            return
        
        elif (mid+1 > len(nums)) and nums[mid-1] < nums[mid]:
            print("con3")
            self.peak = mid
            return

        elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            print("con4")
            self.peak = mid
            return
    
       
        if mid-1 >= 0 and nums[mid-1] > nums[mid]:
            print("con5")
            self.bisect_left(nums,low,mid)

        elif nums[mid+1] > nums[mid]:
            print("con6")
            self.bisect_left(nums, mid+1, high)
        
        return

        
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        self.peak = 0

        self.bisect_left(nums, 0, n-1)
        return self.peak