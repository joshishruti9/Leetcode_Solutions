# Last updated: 3/25/2025, 11:01:30 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from queue import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hmap = dict()
        queue = deque()
        root = node
        visited = set()
        queue.append(node)
        visited.add(node)
        hmap[node] = Node(val = node.val)
        while queue:
            node = queue.popleft()
            copy_node = hmap[node]
            for neighbour in node.neighbors:
                if neighbour not in visited:
                    copy_neighbour_node = Node(val = neighbour.val)
                    copy_node.neighbors.append(copy_neighbour_node)
                    #copy_neighbour_node.neighbors.append(copy_node)
                    hmap[neighbour] = copy_neighbour_node
                    queue.append(neighbour)
                    visited.add(neighbour)
                else:
                    copy_neighbour_node = hmap[neighbour]
                    copy_node.neighbors.append(copy_neighbour_node)
                    #copy_neighbour_node.neighbors.append(copy_node)
        return hmap[root]