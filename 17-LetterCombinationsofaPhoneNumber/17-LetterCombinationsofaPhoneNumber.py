# Last updated: 4/7/2025, 4:26:53 PM
class Solution:
        
    def traverse(self, digits, curr_index, hmap, output, curr_output):

        if len(curr_output) == len(digits):
            output.append(curr_output)
            return

        digit = digits[curr_index]
        letters = hmap[digit]
        for letter in letters:
            self.traverse(digits, curr_index+1, hmap, output, curr_output+letter)
        
        return output



    def letterCombinations(self, digits: str) -> List[str]:

        hmap = {'2' :list('abc'),'3':list('def'),'4':list('ghi'),'5':list('jkl'),'6':list('mno'),'7':list('pqrs'),'8':list('tuv'),'9':('wxyz')}

        output = []
        if len(digits) == 0:
            return output

        output = self.traverse(digits, 0, hmap, output, "")

        return output