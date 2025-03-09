class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = moves.count("U") == moves.count("D") 
        vertical = moves.count("L") == moves.count("R") 
        return(horizontal and vertical)
        