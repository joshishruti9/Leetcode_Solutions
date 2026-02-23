1from heapq import heappop, heappush
2from collections import defaultdict
3
4class Solution:
5    def create_adj_list(self, flights):
6
7        adj_list = defaultdict(list)
8
9        for src, dest, cost in flights:
10            adj_list[src].append((dest, cost))
11        
12        return adj_list
13
14    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
15        adj_list = self.create_adj_list(flights)
16        heap = []
17        visited = {}
18
19        heappush(heap,(0, -1, src))
20
21        while heap:
22            so_far_cost, curr_stop, curr_pos = heappop(heap)
23        
24            print(curr_pos," ",curr_stop," ",so_far_cost)
25            neighbours = adj_list[curr_pos]
26
27            if curr_pos == dst and curr_stop <= k:
28                return so_far_cost
29
30            if curr_stop >= k:
31                continue
32
33            if curr_pos in visited and visited[curr_pos] <= curr_stop:
34                continue
35            
36            visited[curr_pos] = curr_stop
37
38            for next_node, cost in neighbours:
39                curr_cost = so_far_cost + cost
40                heappush(heap, (curr_cost, curr_stop+1, next_node))
41        
42        return -1