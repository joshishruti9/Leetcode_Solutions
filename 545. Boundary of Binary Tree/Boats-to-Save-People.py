1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4
5        i = 0
6        j = len(people)-1
7        count = 0
8
9        while i <= j:
10            if people[i] + people[j] <= limit:
11                count += 1
12                i += 1
13                j -= 1
14            else:
15                j -= 1
16                count += 1
17        
18        if i == j:
19            count += 1
20        return count
21        