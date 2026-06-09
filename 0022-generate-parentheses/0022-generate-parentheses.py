class Solution:
    def backtrack(self, open_count, close_count, curr_res, n):
        if open_count == n and close_count == n:
            self.output.append("".join(curr_res[:]))
            return
        
        if open_count < n:
            curr_res.append("(")
            self.backtrack(open_count+1, close_count, curr_res, n)
            curr_res.pop()
        
        if close_count < open_count:
            curr_res.append(")")
            self.backtrack(open_count, close_count+1, curr_res, n)
            curr_res.pop()

    def generateParenthesis(self, n: int) -> List[str]:

        self.output = []
        self.backtrack(0, 0, [], n)

        return self.output

        