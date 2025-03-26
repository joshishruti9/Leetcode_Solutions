# Last updated: 3/25/2025, 11:46:49 PM
from collections import deque
class Solution:
    def create_adj_list(self, prerequisites):
        adj_list = dict()
        for dest, src in prerequisites:
            if src not in adj_list:
                adj_list[src] = [dest]
            else:
                adj_list[src].append(dest)
        return adj_list
    
    def create_counter(self, adj_list):
        counter = dict()
        for src, dest in adj_list:
            if src in counter:
                counter[src] += 1
            else:
                counter[src] = 1
        return counter
    
    def find_root(self, counter, nums):
        roots = deque()
        for num in range(nums):
            if num not in counter:
                roots.append(num)
        return roots
    
    def traverse_course(self, adj_list, counter, queue):
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            neighbours = adj_list.get(course,[])
            for neighbour in neighbours:
                counter[neighbour] -= 1
                if counter[neighbour] == 0:
                    queue.append(neighbour)
                    counter.pop(neighbour)

        return result if len(counter) == 0 else []


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = self.create_adj_list(prerequisites)
        counter = self.create_counter(prerequisites)
        roots = self.find_root(counter, numCourses)
        return self.traverse_course(adj_list,counter,roots)
        
        