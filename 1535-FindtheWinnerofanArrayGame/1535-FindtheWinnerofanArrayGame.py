# Last updated: 8/8/2025, 12:54:31 PM
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = float("-inf")
        prev_winner = float("-inf")
        count = 0

        i = 0
        j = 1

        while j < len(arr):
           
            winner = max(arr[0], arr[j])
            j += 1
            arr[0] = winner

            if winner == prev_winner:
                count += 1
            else:
                count = 1
            prev_winner = winner

            if count == k:
                break
        
        return winner