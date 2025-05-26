# Last updated: 5/25/2025, 7:50:19 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for letter in stones:
            if letter in jewel_set:
                count += 1
        
        return count