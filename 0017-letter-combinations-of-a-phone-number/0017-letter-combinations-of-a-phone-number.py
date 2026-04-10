class Solution:
    def backtrack(self, digits, i, curr_res):
        if i == len(digits):
            self.res.append("".join(curr_res))
            return
        
        letters = self.hmap[digits[i]]

        for letter in letters:
            curr_res.append(letter)
            self.backtrack(digits, i+1, curr_res)
            curr_res.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.hmap = {'2' :list('abc'),'3':list('def'),'4':list('ghi'),'5':list('jkl'),'6':list('mno'),'7':list('pqrs'),'8':list('tuv'),'9':('wxyz')}

        self.res = []
        self.backtrack(digits, 0, [])

        return self.res

        
        