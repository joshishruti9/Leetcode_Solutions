# Last updated: 4/13/2025, 9:57:25 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        index = 0
        n = len(arr)-1
        j = arr[n]
        missing_num = []

        while i < j+1:
            if arr[index] != i:
                missing_num.append(i)
            else:
                index += 1

            i += 1

        if k <= len(missing_num):
            return missing_num[k-1]
        else:
            k = k -len(missing_num)
            while k > 0:
                i += 1
                k -= 1
            return i-1

        