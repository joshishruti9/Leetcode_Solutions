class Solution:
    def calculate_distance(self, x, y, x1, y1):
        
        dist = ((abs(x1-x)) ** 2 + (abs(y1-y)) ** 2) ** 0.5
        return dist
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        
        #to represent the postion of warehouse
        x = 0
        y = 0
        
        for x1, y1 in points:
            dist = self.calculate_distance(x, y, x1, y1)
            
            if len(max_heap) < k:
                heappush(max_heap, (-dist, x1, y1))
            else:
                popped_dist, popped_x1, popped_y1 = heappop(max_heap)
                
                popped_dist = popped_dist * -1
                
                if dist < popped_dist:
                    heappush(max_heap, (-dist, x1, y1))
                else:
                    heappush(max_heap, (-popped_dist, popped_x1, popped_y1))
                    
        res = []
        for i in range(k):
            res.append((max_heap[i][1], max_heap[i][2]))
            
        return res
        