"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        queue = deque()
        hmap = {}
        root = node
        queue.append(node)
        visited = set()
        visited.add(node)
        new_node = Node(node.val)
        hmap[node] = new_node 
        
        while queue:
            popped_node = queue.popleft()
            new_node = hmap[popped_node]

            neighbour_nodes = popped_node.neighbors

            for neighbour_node in neighbour_nodes:
                if neighbour_node not in visited:
                    new_neighbour = Node(neighbour_node.val)
                    new_node.neighbors.append(new_neighbour)
                    hmap[neighbour_node] = new_neighbour
                    queue.append(neighbour_node)
                    visited.add(neighbour_node)
                else:
                    new_neighbour = hmap[neighbour_node]
                    new_node.neighbors.append(new_neighbour)
        
        return hmap[root]
        