# Last updated: 8/20/2025, 1:00:54 AM
from heapq import heappush, heappop
from collections import deque

class Solution:
    def create_adj_list(self, equations, values):
        i = 0
        adj_list = {}
        for src, dest in equations:
            if src in adj_list:
                adj_list[src].append((dest, values[i]))
            else:
                adj_list[src] = [(dest, values[i])]

            if dest in adj_list:
                adj_list[dest].append((src, 1/values[i]))
            else:
                adj_list[dest] = [(src, 1/values[i])]
            
            i += 1
        
        return adj_list

    def find_division(self, src, dest, adj_list):

        queue = deque()
        visited = set()

        queue.append((1,src))
        visited.add(src)

        while queue:
            curr_mul, node = queue.popleft()
            neighbours = adj_list.get(node, [])

            if node == dest:
                return curr_mul

            for neighbour, num in neighbours:
                mul = curr_mul * num

                if neighbour not in visited:
                    queue.append((mul,neighbour))
                    visited.add(neighbour)

        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = self.create_adj_list(equations, values)
        print(adj_list)
        res = []

        for src, dest in queries:
            if src not in adj_list or dest not in adj_list:
                res.append(-1.0)
                continue
            
            if src == dest:
                res.append(1.0)
                continue

            ans = self.find_division(src, dest, adj_list)
            res.append(ans)
        
        return res
        