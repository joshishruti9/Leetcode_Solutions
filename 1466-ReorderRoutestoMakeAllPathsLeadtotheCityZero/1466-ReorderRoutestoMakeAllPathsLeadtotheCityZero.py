# Last updated: 8/6/2025, 2:59:42 PM
from collections import deque
class Solution:
    def reorder_count(self, adj_list):
        visited = set()
        queue = deque() 
        queue.append(0)
        visited.add(0)
        count = 0

        while queue:
            node = queue.popleft()
            node_dict = adj_list.get(node, {})
            for out in node_dict.get('out', []):
                if out not in visited:
                    count += 1
                    queue.append(out)
                    visited.add(out)
            
            for innode in node_dict.get("in",[]):
                if innode not in visited:
                    queue.append(innode)
                    visited.add(innode)
                
        return count


    def create_adjList(self, connections, n):
        adj_list = dict()
        for u, v in connections:
            if u not in adj_list: adj_list[u] = {'out': [], 'in': []}
            if v not in adj_list: adj_list[v] = {'out': [], 'in': []}

            adj_list[u]["out"].append(v)
            adj_list[v]["in"].append(u)
        
        return adj_list

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adj_list = self.create_adjList(connections,n)
        
        count = self.reorder_count(adj_list)

        return count