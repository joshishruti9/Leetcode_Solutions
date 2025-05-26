# Last updated: 5/25/2025, 6:49:22 PM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        
        for hour in hours:
            if hour >= target:
                count += 1
        
        return count