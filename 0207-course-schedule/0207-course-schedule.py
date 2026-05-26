from collections import deque

class Solution:
    def find_root(self, numCourses, pre_counter):
        roots = deque()
        
        for num in range(numCourses):
            if num not in pre_counter:
                roots.append(num)

        return roots

    # create how many are pending for each course to finish
    def prerequisite_counter(self, prerequisites):
        hmap = {}

        for dest, src in prerequisites:
            if dest in hmap:
                hmap[dest] += 1
            else:
                hmap[dest] = 1
        
        return hmap


    def create_adjList(self, prerequisites):
        adj_list = {}

        for dest, src in prerequisites:
            if src in adj_list:
                adj_list[src].append(dest)
            else:
                adj_list[src] = [dest]
        
        return adj_list
    
    def traverse(self, queue, adj_list, counter):
        visited = len(queue)
        while queue:
            node = queue.popleft()
            courses = adj_list.get(node,[])

            for course in courses:
                counter[course] -= 1

                if counter[course] == 0:
                    queue.append(course)
                    visited += 1

        return visited


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        adj_list = self.create_adjList(prerequisites)
        pre_counter = self.prerequisite_counter(prerequisites)
        roots = self.find_root(numCourses, pre_counter)
        count = self.traverse(roots, adj_list, pre_counter)

        return count == numCourses

        