class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        character_map = {}

        occured_characters = set()

        for s_char, t_char in zip(s, t):
            if s_char in character_map:
                if t_char != character_map[s_char]:
                    return False
                else:
                    continue
            if t_char in occured_characters:
                return False

            character_map[s_char] = t_char 
            occured_characters.add(t_char)

        return True       