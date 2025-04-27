# Last updated: 4/27/2025, 2:25:10 PM
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        max_len = 0
        for i in range(1, n - 1): 
            if arr[i - 1] < arr[i] > arr[i + 1]: 
                left = i - 1
                right = i + 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1            
                max_len = max(max_len, right - left + 1)
    
        return max_len
        