from heapq import heappush, heappop

class Solution:
    def create_adj_list(self, n, flights):
        adj_list = {}
        for src, dest, cost in flights:
            if src not in adj_list:
                adj_list[src] = [(dest, cost)]
            else:
                adj_list[src].append((dest, cost))
        
        return adj_list
            
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = self.create_adj_list(n, flights)

        heap = []
        min_price = float("inf")

        neighbours = adj_list.get(src, [])
        visited = set()

        if len(neighbours) == 0:
            return -1
        
        for dest, cost in neighbours:
            heappush(heap, (cost, 0, dest))
        
        visited = {}

        while heap:
            curr_cost, curr_k, curr_dest = heappop(heap)

            if curr_k <= k and curr_dest == dst:
                return curr_cost
            
            if curr_k > k or (curr_k == k and curr_dest != dst):
                continue
            
            if (curr_dest, curr_k) in visited:
                if visited[(curr_dest, curr_k)] < curr_cost:
                    continue
            
            next_dest = adj_list.get(curr_dest, [])

            for dest, cost in next_dest:
                if curr_cost + cost < visited.get((dest, curr_k+1), float("inf")):
                    visited[(dest, curr_k+1)] = (curr_cost+cost)
                    heappush(heap, ((curr_cost + cost), curr_k+1, dest))
        
        return -1