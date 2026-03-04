1from heapq import heappop, heappush
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4
5        heap = []
6        for stone in stones:
7            heappush(heap,-stone)
8        
9        while len(heap) > 1:
10            x = heappop(heap) * -1
11            y = heappop(heap) * -1
12        
13            if x != y:
14                heappush(heap,-(x-y))
15
16        
17        return 0 if len(heap) == 0 else (heappop(heap)*-1)
18
19
20