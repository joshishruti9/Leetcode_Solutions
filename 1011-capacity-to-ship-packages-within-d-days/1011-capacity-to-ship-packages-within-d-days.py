class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) / 2
            curr_weight = 0
            day_need = 1

            for weight in weights:
                if curr_weight + weight > mid:
                    day_need += 1
                    curr_weight = 0
                curr_weight += weight
            if day_need > D: 
                left = mid + 1
            else: 
                right = mid

        return math.floor(left)