# Last updated: 7/6/2025, 6:40:02 PM
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length = 0
        i = 0
        length = 0
        flag = False
        n = len(arr)

        while i < n-1:
            while i < n-1 and arr[i] >= arr[i+1]:
                i += 1
 
            start = i
            print("start ",start)

            while i < n-1 and arr[i] < arr[i+1]:
                i += 1
            
            peak = i
            print("peak ",peak)

            while i < n-1 and arr[i] > arr[i+1]:
                i += 1

            end = i
            print("start ",start)
            print("end ",end)
            
            if peak != end:
                max_length = max(max_length, (end-start+1))
                print("end ",max_length)
            
        return max_length
        