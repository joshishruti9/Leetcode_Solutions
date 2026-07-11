from collections import deque
class Solution:
    def create_adjList(self, edges):
        adj_list = {}
        for start, end in (edges):

            if start in adj_list:
                adj_list[start].append(end)
            else:
                adj_list[start] = [end]

            if end in adj_list:
                adj_list[end].append(start)
            else:
                adj_list[end] = [start]

        return adj_list
    
    def find_neighbours(self, queue, visited, adj_list):
        edge = 0
        num = 0
        while queue:
            node = queue.popleft()
            num += 1
            neighbours = adj_list.get(node,[])
            for neighbour in neighbours:
                edge += 1
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

        edge = edge // 2
        n = (num * (num-1)) // 2
        return True if n == edge else False

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = self.create_adjList(edges)
        visited = set()
        queue = deque()
        count = 0

        for i in range(n):
            if i not in visited:
                queue.append(i)
                visited.add(i)
                if self.find_neighbours(queue, visited, adj_list):   
                    count += 1

        return count