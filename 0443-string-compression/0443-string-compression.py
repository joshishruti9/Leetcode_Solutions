class Solution:
    def add_count(self, chars, k, count):
        nums = []

        while count > 0:
            nums.append(count % 10)
            count //= 10
        
        for i in range(len(nums)-1, -1, -1):
            chars[k] = str(nums[i])
            k += 1
        
        return k

    def compress(self, chars: List[str]) -> int:

        original = chars[:]   # keep original values for reading

        i = 1
        count = 0
        flag = False
        n = len(original)
        k = 0

        if n == 1:
            return 1

        while i < n:
            if original[i] == original[i-1]:
                flag = True
                count += 1
                i += 1
            else:
                if flag:
                    chars[k] = original[i-1]
                    k = self.add_count(chars, k+1, count+1)
                else:
                    chars[k] = original[i-1]
                    k += 1
                
                count = 0
                i += 1
                flag = False

        # handle last group
        if original[n-1] == original[n-2]:
            count += 1
            chars[k] = original[i-1]
            k = self.add_count(chars, k+1, count)
            return k
        else:
            chars[k] = original[n-1]
            return k + 1