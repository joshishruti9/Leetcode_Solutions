# Last updated: 8/11/2025, 4:43:34 PM
from heapq import heappush, heappop
class Solution:
    def create_adjList(self, edges, succProb):
        adj_list = {}
        for i, (start, end) in enumerate(edges):

            if start in adj_list:
                adj_list[start].append((end, succProb[i]))
            else:
                adj_list[start] = [(end,succProb[i])]

            if end in adj_list:
                adj_list[end].append((start, succProb[i]))
            else:
                adj_list[end] = [(start,succProb[i])]

        return adj_list

    def find_neighbour(self, visited, pri_queue, end, adj_list):
        while pri_queue:
            prob, node = heappop(pri_queue)
            neighbours = adj_list.get(node,[])
            prob = prob * -1

            if node == end:
                self.res = max(self.res, prob)
                return

            for neighbour, succProb in neighbours:
                curr_prob = prob * succProb
                if curr_prob <= visited.get(neighbour,0):
                    continue

                heappush(pri_queue,(-curr_prob,neighbour))
                visited[neighbour] = curr_prob                   
       
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_list = self.create_adjList(edges, succProb)
        visited = {}
        pri_queue = []
        heappush(pri_queue,(-1.0,start_node))
        visited[start_node] = 1.0

        self.res = 0.0
        
        self.find_neighbour(visited, pri_queue, end_node, adj_list)
        
        return self.res