# Last updated: 6/25/2025, 3:07:52 PM
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = set()

        i = 1
        count = 1
        res = []

        while i not in visited:        
            visited.add(i)
            i = i + (count * k)
            count += 1
            if i > n:
                i = i % n
                if i == 0:
                    i = n - i
        
        print(visited)
        for i in range(1,n+1):
            if i not in visited:
                res.append(i)
        
        return res