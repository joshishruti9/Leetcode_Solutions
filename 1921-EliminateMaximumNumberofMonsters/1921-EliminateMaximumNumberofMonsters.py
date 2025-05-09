# Last updated: 5/9/2025, 2:06:42 PM
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [0 for i in range(len(dist))]
        for i in range(len(dist)):
            time[i] = dist[i] / speed[i]
        
        time.sort()

        for i in range(len(time)):
            if time[i] <= i:
                return i
            
        return len(time)

        