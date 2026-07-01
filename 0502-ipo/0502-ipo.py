from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        max_heap = []
        projects = []

        for i in range(len(profits)):
            projects.append((capital[i], profits[i]))
        
        projects.sort()
        j = 0

        for i in range(k):
            
            while j < len(projects) and projects[j][0] <= w:
                heappush(max_heap, -projects[j][1])
                j += 1
            
            if not max_heap:
                break
            
            w -= heappop(max_heap)
        
        return w
            


        