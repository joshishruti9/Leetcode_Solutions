from heapq import heappush, heappop
class Solution:
    def calculate_distance(self, x, y):
        return ((x ** 2) + (y ** 2)) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        closest_points = []

        for point in points:
            dist = self.calculate_distance(point[0], point[1])
            heappush(closest_points, (dist, point))
        
        res = []
        for i in range(k):
            dist, point = heappop(closest_points)
            res.append(point)
        
        return res
        