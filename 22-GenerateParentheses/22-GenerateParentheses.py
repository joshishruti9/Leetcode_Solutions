# Last updated: 5/20/2025, 2:23:43 PM
class Solution:
    def traverse(self, open_count, close_count, n, curr_res):
        if close_count == n and open_count == n:
            self.output.append("".join(curr_res[:])) 
            return
        
        if open_count < n:
            curr_res.append('(')
            self.traverse(open_count+1, close_count, n, curr_res)
            curr_res.pop()
        
        if close_count < open_count:
            curr_res.append(')')
            self.traverse(open_count, close_count+1, n, curr_res)
            curr_res.pop()  

    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.traverse(0,0,n,[])

        return self.output