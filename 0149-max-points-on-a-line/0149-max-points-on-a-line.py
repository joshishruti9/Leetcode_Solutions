class Solution:
    def calculate_slope(self, x1, y1, x2, y2):
        if x1 == x2:
            return float("inf")

        return (y2 - y1) / (x2 - x1)

    def maxPoints(self, points: List[List[int]]) -> int:

        max_num = 0

        for i, point in enumerate(points):
            slope_map = {}
            for j in range(i+1, len(points)):
                slope_val = self.calculate_slope(point[0], point[1], points[j][0], points[j][1])
                if slope_val in slope_map:
                    slope_map[slope_val] += 1
                else:
                    slope_map[slope_val] = 1
            
            if slope_map:
                max_slope = max(slope_map.values())
                max_num = max(max_num, max_slope + 1)
            else:
                max_num = max(max_num, 1)

        return max_num 





        