# Last updated: 7/6/2025, 6:47:18 PM
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        res = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l,r = i-1,i+1

                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1

                while r < len(arr)-1 and arr[r+1] < arr[r]:
                    r += 1

                res = max(res,r-l+1)


        return res
                
            
