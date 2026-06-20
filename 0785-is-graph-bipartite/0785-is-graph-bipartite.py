from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        queue = deque()
        visited = set()
        # value is going to be either 0 or 1 
        neighbour_group = [-1] * len(graph)

        for i in range(len(graph)):
            queue.append(i)
            visited.add(i)
            
            while queue:
                node = queue.popleft()
                neighbours = graph[node]

                for neighbour in neighbours:
                    #both are new
                    if neighbour_group[neighbour] == -1 and neighbour_group[node] == -1:
                        neighbour_group[neighbour] = 0
                        neighbour_group[node] = 1
                    #node is present
                    elif neighbour_group[neighbour] == -1:
                        neighbour_group[neighbour] = 1 - neighbour_group[node]
                    elif neighbour_group[node] == -1:
                        neighbour_group[node] = 1 - neighbour_group[neighbour]
                    else:
                        if neighbour_group[node] == neighbour_group[neighbour]:
                            return False
                    

                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
        
        return True        