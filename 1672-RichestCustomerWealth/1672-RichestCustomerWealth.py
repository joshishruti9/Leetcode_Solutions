# Last updated: 5/24/2025, 8:30:15 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_total = 0
        total = 0

        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                total += accounts[i][j]
            max_total = max(max_total, total)
            total = 0
        
        return max_total
        