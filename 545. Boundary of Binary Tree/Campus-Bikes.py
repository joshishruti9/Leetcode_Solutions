1class Solution:
2    def calculate_distance(self, p1, p2, x, y):
3        return (abs(p1 - x) + abs(p2 - y))
4
5    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
6        
7        #iterate over bike and for each bike calculate distance with each worker. bike with  minimum distance with worker put it as a list into hashmap. now continue to this and skip bike already present in hashmap
8
9        hmap = {}
10        reverse_map = defaultdict(list)
11        min_dist = float("inf")
12        res = [-1 for i in range(len(workers))]
13
14        for i in range(len(workers)):
15            for j in range(len(bikes)):
16                ans = self.calculate_distance(workers[i][0], workers[i][1], bikes[j][0], bikes[j][1])
17                hmap[(i,j)] = ans
18                reverse_map[ans].append((i,j))
19        
20
21        sorted_dist = sorted(hmap.items(), key = lambda item: item[1])
22        bike_visited = set()
23
24        for (worker_index, bike_index), val in sorted_dist:
25            if bike_index in bike_visited or res[worker_index] != -1:
26                continue
27
28            bike_visited.add(bike_index)
29            res[worker_index] = bike_index
30
31
32        return res 
33
34
35
36        
37        '''
38        for val in sorted_dist:
39            values = reverse_map.get(val)
40            values.sort()
41            for i in range(len(values)):
42                if values[i][0] not in visited: 
43                    res.append([values[i][0], values[i][1]])
44                    visited.add(values[i][0])
45        '''
46
47        return res
48
49
50
51        