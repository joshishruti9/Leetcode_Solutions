from collections import deque

class Solution:
    def traverse(self, adj_list, queue, visited):
    
        while queue:
            node = queue.popleft()
            neighbours = adj_list.get(node, [])

            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    def create_adjList(self, n, connections):
        adj_list = {}

        for src, dest in connections:
            if src not in adj_list:
                adj_list[src] = [dest]
            else:
                adj_list[src].append(dest)
            

            if dest not in adj_list:
                adj_list[dest] = [src]
            else:
                adj_list[dest].append(src)

        
        return adj_list
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        adj_list = self.create_adjList(n, connections)

        total_edges = 0
        component_count = 0

        for i in range(n):
            if i not in visited:
                queue.append(i)
                visited.add(i)
                self.traverse(adj_list, queue, visited)
                component_count += 1

        total_edges = len(connections)

        return component_count-1 if total_edges >= n-1 else -1

        