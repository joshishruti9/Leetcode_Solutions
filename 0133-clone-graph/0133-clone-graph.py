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

        if node is None:
            return None
        

        head = node
        queue = deque()
        visited = set()
        queue.append(node)
        visited.add(node)
        hmap = {}

        while queue:
            old_node = queue.popleft() 
            neighbour_nodes = old_node.neighbors

            if old_node not in hmap:
                new_node = Node(old_node.val)
                hmap[old_node] = new_node
            else:
                new_node = hmap[old_node]

            for neighbor in neighbour_nodes:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

                if neighbor not in hmap:
                    new_neighbour_node = Node(neighbor.val)
                    hmap[neighbor] = new_neighbour_node
                else:
                    new_neighbour_node = hmap[neighbor]

                new_node.neighbors.append(new_neighbour_node)
            
            
        
        return hmap[head]


        

