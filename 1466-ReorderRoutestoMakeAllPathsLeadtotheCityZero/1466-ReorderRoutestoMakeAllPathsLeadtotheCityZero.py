# Last updated: 7/6/2025, 2:43:49 PM
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        seen = {0}

        graph = defaultdict(list)

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))
        
        def dfs(node):
            ans = 0
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    if (node, n) in roads:
                        ans+=1
                    ans+=dfs(n)
            return ans

        return dfs(0)