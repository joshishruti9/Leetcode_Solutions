class Solution:
    def find_root(self, counter, numCourses):
        queue = deque()
        for num in range(numCourses):
            if num not in counter:
                queue.append(num)
        
        return queue
    
    def create_adjList(self, prerequisites):
        adj_list = {}
        for dest, src in prerequisites:
            if src not in adj_list:
                adj_list[src] = [dest]
            else:
                adj_list[src].append(dest)
        
        return adj_list
    
    def create_prerequisiteMap(self, adj_list):
        counter = {}

        for dest, src in adj_list:
            if dest not in counter:
                counter[dest] = 1
            else:
                counter[dest] += 1
        
        return counter
    
    def traverse(self, adj_list, queue, counter):
        
        visited = set(queue)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            neighbors = adj_list.get(node, [])

            for neighbor in neighbors:
                if neighbor in counter:
                    counter[neighbor] -= 1
                    if counter[neighbor] == 0:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        return res

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = self.create_adjList(prerequisites)
        counter = self.create_prerequisiteMap(prerequisites)
        queue = self.find_root(counter, numCourses)
        res = self.traverse(adj_list, queue, counter)

        print(res)
        return res if len(res) == numCourses else []