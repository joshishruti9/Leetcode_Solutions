class Solution:
    def traverse(self, digits, curr_index, curr_res):

        if len(curr_res) == len(digits):
            self.res.append("".join(curr_res))
            return
        
        digit = digits[curr_index]
        letters = self.hmap[digit]

        for letter in letters:
            curr_res.append(letter)
            self.traverse(digits, curr_index+1, curr_res)
            curr_res.pop()
        
        return


    def letterCombinations(self, digits: str) -> List[str]:

        self.hmap = {'2' :list('abc'),'3':list('def'),'4':list('ghi'),'5':list('jkl'),'6':list('mno'),'7':list('pqrs'),'8':list('tuv'),'9':('wxyz')}

        self.res = []

        self.traverse(digits, 0, [])

        return self.res





        