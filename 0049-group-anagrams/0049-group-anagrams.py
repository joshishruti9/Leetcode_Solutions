class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
        
        res = []
        for value in word_map.values():
            res.append(value)
        
        return res
        