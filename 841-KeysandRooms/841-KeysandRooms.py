# Last updated: 7/6/2025, 4:18:22 PM
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        start = 0
        queue = deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            num = queue.popleft()
            nodes = rooms[num]
            for node in nodes:
                if node not in visited:
                    queue.append(node)
                    visited.add(node) 

        return len(rooms) == len(visited)