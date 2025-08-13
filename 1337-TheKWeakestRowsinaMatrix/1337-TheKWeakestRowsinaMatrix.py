# Last updated: 8/13/2025, 2:55:46 PM
from heapq import heappush, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        res = []
        m = len(mat)

        for i, row in enumerate(mat):
            count = sum(row)
            if len(arr) < k:
                heappush(arr, (-count, -i))
            else:
                count1, j = heappop(arr)
                if count < -count1 or (count == -count1 and i < -j) :
                    heappush(arr,(-count,-i))
                else:
                    heappush(arr,(count1,j))

        while arr:
            count, i = heappop(arr)
            res.append(-i)
        
        return res[::-1]