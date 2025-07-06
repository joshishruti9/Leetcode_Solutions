# Last updated: 7/6/2025, 4:41:24 PM
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
        
        return 0 if (max_len==0 and(end == start or start == peak or end == peak)) else max_len
       
        