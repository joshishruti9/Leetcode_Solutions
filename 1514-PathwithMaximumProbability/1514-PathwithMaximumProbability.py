# Last updated: 8/11/2025, 2:35:52 PM
from collections import deque
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

    def find_neighbour(self, visited, queue, end, adj_list):
        while queue:
            node, prob = queue.popleft()
            neighbours = adj_list.get(node,[])

            for neighbour, succProb in neighbours:
                curr_prob = prob * succProb
                if neighbour in visited:
                    if curr_prob <= visited.get(neighbour,0):
                        continue
                if neighbour == end:
                        self.res = max(self.res, curr_prob)
                queue.append((neighbour,curr_prob))
                visited[neighbour] = curr_prob
                
                      
       
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_list = self.create_adjList(edges, succProb)
        visited = {}
        queue = deque()
        queue.append((start_node,1))
        visited[start_node] = 1.0

        self.res = 0.0
        
        self.find_neighbour(visited, queue, end_node, adj_list)
        
        return self.res