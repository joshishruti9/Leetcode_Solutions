# Last updated: 8/7/2025, 8:52:36 PM
from collections import Counter
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []

        counter = {}

        for name in names:
            if name in counter:
                while name+"("+str(counter[name])+")" in counter:
                    counter[name] += 1
                new_name = name+"("+str(counter[name])+")"
                ans.append(new_name)
                counter[name] += 1
                counter[new_name] = 1
            else:
                ans.append(name)
                counter[name] = 1
            
        return ans