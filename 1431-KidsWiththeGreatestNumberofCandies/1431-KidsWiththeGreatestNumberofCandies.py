# Last updated: 5/25/2025, 6:41:45 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        
        return res
        