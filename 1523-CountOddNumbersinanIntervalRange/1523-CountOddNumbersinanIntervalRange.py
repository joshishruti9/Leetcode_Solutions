# Last updated: 8/13/2025, 2:18:58 PM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total_num = (high - low) + 1

        if low % 2 != 0:
            if total_num % 2 == 0:
                return total_num // 2
            else:
                return (total_num // 2) + 1
        else:
            return total_num // 2