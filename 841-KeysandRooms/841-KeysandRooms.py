# Last updated: 4/4/2025, 2:42:55 PM
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        while queue:
            room = queue.popleft()
            for room in rooms[room]:
                if room not in visited:
                    queue.append(room)
                    visited.add(room)

        return len(visited) == len(rooms)