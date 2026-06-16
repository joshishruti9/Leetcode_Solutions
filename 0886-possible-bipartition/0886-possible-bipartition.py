from collections import deque
class Solution:
    def create_adjList(self, dislikes, n):
        adj_list = {}

        for i, j in dislikes:
            if i in adj_list:
                adj_list[i].append(j)
            else:
                adj_list[i] = [j]
            
            if j in adj_list:
                adj_list[j].append(i)
            else:
                adj_list[j] = [i]
        
        return adj_list

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        if len(dislikes) == 0:
            return True

        adj_list = self.create_adjList(dislikes, n)
        color = [-1 for i in range(n+1)]

        queue = deque()
        visited = set()

        for i in range(1, n+1):
            if i in visited:
                continue

            queue.append(i)
            visited.add(i)

            while queue:
                node = queue.popleft()
                neighbours = adj_list.get(node,[])

                for neighbour in neighbours:    
                    if color[neighbour] == -1 and color[node] == -1:
                        color[neighbour] = 1
                        color[node] = 1 - color[neighbour]
                    elif color[neighbour] != -1 and color[node] != -1:
                        if  color[neighbour] == color[node]:
                            return False
                    elif color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]

                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

        return True 

        


        