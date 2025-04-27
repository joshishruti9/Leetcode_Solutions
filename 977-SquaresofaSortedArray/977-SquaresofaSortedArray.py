# Last updated: 4/27/2025, 2:22:24 PM
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 0
        start = end = peak = 0

        while i < n-1:
            while i < n-1 and arr[i] >= arr[i+1]:
                i += 1
            
            if i == n:
                return max_len

            start = i

            while i < n-1 and arr[i] < arr[i+1] :
                i += 1
            
            if i == n:
                return max_len

            peak = i
            

            while i < n-1 and arr[i] > arr[i+1]:
                i += 1
            
            if i == n:
                return max_len
            end = i

            if peak != end:
                max_len = max(max_len, (end-start+1))
        
        print(start," ",end," ",peak," ",max_len)
        return 0 if (max_len==0 and(end == start or start == peak or end == peak)) else max_len
       
        