class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            hmap[sorted_word].append(word)
        
        res = []
        for key, val in hmap.items():
            res.append(val)

        return res