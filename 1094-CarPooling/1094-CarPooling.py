# Last updated: 8/11/2025, 6:56:55 PM
class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        nums = []
        for curr_cap, start, end in trips:
            nums.append((start,curr_cap))
            nums.append((end, -curr_cap))
            

        nums.sort()

        cap = 0
        for time, curr_cap in nums:
            cap += curr_cap

            if cap > capacity:
                return False
        
        return True