class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {'R':(0,1),'L':(0,-1),'U':(1,0),'D':(-1,0)}
        x = y = 0 
        for i in range(len(moves)):
            p1, p2 = directions[moves[i]]
            x = x + p1
            y = y + p2
        
        return x == 0 and y == 0
