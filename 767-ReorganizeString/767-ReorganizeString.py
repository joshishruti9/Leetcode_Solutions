# Last updated: 8/22/2025, 2:13:14 PM
from collections import Counter
from heapq import heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
       
        n = len(s)
        
        if n == 1:
            return s

        counter = dict()
        counter = Counter(s)
        heap = []
        ans = []
        count = ceil(n/2)

        if max(counter.values()) > count:
            return ""

        for key, value in counter.items():
            heappush(heap,(-value,key))
        
        while heap:
            if heap:
                max1, key1 = heappop(heap)
                ans.append(key1)
                max1 = -max1 - 1
            if heap:
                max2, key2 = heappop(heap)
                ans.append(key2)
                max2 = -max2 - 1
            
            if max1 > 0:
                heappush(heap,(-max1, key1))
            if max2 > 0:
                heappush(heap,(-max2, key2))
        
        return "".join(ans)

                    