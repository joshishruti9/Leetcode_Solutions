# Last updated: 5/28/2025, 7:33:37 PM
class Solution:
    def intToRoman(self, num: int) -> str:

        hmap = dict()
        hmap[1000] = 'M'
        hmap[500] = 'D'
        hmap[100] = 'C'
        hmap[50] = 'L'
        hmap[10] = 'X'
        hmap[5] = 'V'
        hmap[1] = 'I'
        hmap[4] = 'IV'
        hmap[9] = 'IX'
        hmap[40] = 'XL'
        hmap[90] = 'XC'
        hmap[400] = 'CD'
        hmap[900] = 'CM'

        keys = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        
        i = 0
        res = []
        while i < len(keys):
            if num >= keys[i]:
                num -= keys[i]
                res.append(hmap[keys[i]])
            else:
                i += 1

        return "".join(res)
        



        
        