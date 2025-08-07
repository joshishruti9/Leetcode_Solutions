# Last updated: 8/6/2025, 8:40:32 PM
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        hmap = dict()
        count = 0

        for i in range(n):
            pref_cnt = 0
            friends = preferences[i]
            fmap = {}
            for friend in friends:
                fmap[friend] = pref_cnt
                pref_cnt += 1
            hmap[i] = fmap

        unhappy = set()
        for i in range(len(pairs)):
            x, y = pairs[i][0], pairs[i][1]
            for j in range(i+1, len(pairs)):
                u, v = pairs[j][0], pairs[j][1]
 
                if hmap[x][u] < hmap[x][y] and hmap[u][x] < hmap[u][v]:
                    unhappy.add(x)
                    unhappy.add(u)

                if hmap[y][u] < hmap[y][x] and hmap[u][y] < hmap[u][v]:
                    unhappy.add(y)
                    unhappy.add(u)
                
                if hmap[x][v] < hmap[x][y] and hmap[v][x] < hmap[v][u]:
                    unhappy.add(x)
                    unhappy.add(v)
                
                if hmap[y][v] < hmap[y][x] and hmap[v][y] < hmap[v][u]:
                    unhappy.add(y)
                    unhappy.add(v)


        return len(unhappy)