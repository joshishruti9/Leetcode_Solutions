# Last updated: 7/14/2025, 10:34:43 PM
from heapq import heappush, heappop
class Solution:
    def find_neighbours(self, movetime, i, j, curr_time, queue, visited):
        m = len(movetime)
        n = len(movetime[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        for di, dj in directions:
            if 0 <= i + di < m and 0 <= j + dj < n:
                time = max(curr_time, movetime[i+di][j+dj])
                if ((i+di,j+dj)) in self.hmap and self.hmap[(i+di, j+dj)] < time+1:
                    continue
                heappush(queue,(time+1, i+di, j+dj))
                self.hmap[(i+di, j+dj)] = time+1
                
    def find_total_time(self, moveTime):
        queue = []
        visited = set()
        m = len(moveTime)
        n = len(moveTime[0])

        heappush(queue, (0,0,0))
        min_time = 0

        while queue:
            time, i, j = heappop(queue)

            if i == m-1 and j == n-1:
                return time
            
            if (i,j) in visited:
                continue
            visited.add((i,j))
        
            self.find_neighbours(moveTime, i, j, time, queue, visited)

        return -1

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        time = 0
        self.hmap = dict()
        min_time = self.find_total_time(moveTime)

        return min_time
        