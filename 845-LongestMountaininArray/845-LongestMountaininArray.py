# Last updated: 4/27/2025, 3:59:00 PM
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 0
        start = end = peak = 0

        while i < n-1:
            while i < n-1 and arr[i] >= arr[i+1]:
                i += 1
            start = i

            while i < n-1 and arr[i] < arr[i+1] :
                i += 1
            peak = i
            
            while i < n-1 and arr[i] > arr[i+1]:
                i += 1
            end = i

            if peak != end:    
                max_len = max(max_len, (end-start+1))
        
        return max_len
       
        