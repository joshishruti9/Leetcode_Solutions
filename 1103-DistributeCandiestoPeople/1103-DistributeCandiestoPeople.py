# Last updated: 8/13/2025, 3:14:17 PM
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        count = 0
        round = 0
        res = [0 for i in range(num_people)]
        turn = 1

        while candies > 0: 
            for i in range(num_people):
                if candies < turn:
                    res[i] += candies
                else:
                    res[i] += turn
                
                candies -= turn
                turn += 1
                if candies <= 0:
                    return res 
        
        return res