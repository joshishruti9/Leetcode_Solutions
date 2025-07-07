# Last updated: 7/6/2025, 7:26:09 PM
from collections import deque

class Solution:
    def find_watchedvideos(self, nodes, watchedVideos):
        frequency = dict()
        for node in nodes:
            videos = watchedVideos[node]
            for video in videos:
                if video in frequency:
                    frequency[video] += 1
                else:
                    frequency[video] = 1
        
        return frequency

    def bfs(self, friends, queue, visited, level):
        res = []
        while queue:
            node, curr_level = queue.popleft()
            friendlist = friends[node]

            if curr_level == level:
                res.append(node) 
            else:
                for member in friendlist:
                    if member not in visited:
                        queue.append((member, curr_level+1))
                        visited.add(member)
        
        return res

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        queue = deque()
        visited = set()

        queue.append((id,0))
        visited.add(id)

        res = self.bfs(friends, queue, visited, level)
      
        frequency = self.find_watchedvideos(res, watchedVideos)

        def sort_func(key):
            return (frequency[key], key)
     
        ans = sorted(frequency, key = sort_func)

        return ans