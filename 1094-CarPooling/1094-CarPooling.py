# Last updated: 8/10/2025, 1:48:57 AM
class Solution:
    def find_trip_possibility(self, trips, capacity):
        curr_capacity = capacity
        prev_end = 0
        prev_trip = []
        i = 0

        for cust, start, end in trips:
            i = 0
            while i < len(prev_trip):
                prev_cust, prev_end = prev_trip[i]
                if start >= prev_end:
                    curr_capacity += prev_cust
                    prev_trip.pop(i)
                else:
                    i += 1
                
            if cust <= curr_capacity:
                curr_capacity -= cust
            else:
                return False
        
            prev_trip.append((cust, end))

        return True


    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def sort_func(trips):
            return trips[1]

        trips.sort(key = sort_func)
        return self.find_trip_possibility(trips, capacity)