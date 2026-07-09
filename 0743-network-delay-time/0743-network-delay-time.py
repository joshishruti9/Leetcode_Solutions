from heapq import heappush, heappop

class Solution:
    def create_adjList(self, times):
        adj_list = {}

        for u, v, time in times:
            if u in adj_list:
                adj_list[u].append((v, time))
            else:
                adj_list[u] = [(v, time)]
        
        return adj_list

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = self.create_adjList(times)

        min_heap = []
        visited = set()
        min_time = float("inf")

        heappush(min_heap, (0, k))

        while min_heap:
            so_far_time, node = heappop(min_heap)

            visited.add(node)

            if len(visited) == n:
                min_time = min(min_time, so_far_time)
                break

            neighbours = adj_list.get(node, [])

            for neighbour_node, time in neighbours:
                if neighbour_node not in visited:
                    heappush(min_heap, (time + so_far_time, neighbour_node))
        
        return min_time if min_time != float("inf") else -1