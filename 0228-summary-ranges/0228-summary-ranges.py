class Solution:
    # Here we will go throgh numbers and check if next number is greater than current number by one if yes we will increment j
    #If no we will append i->j in result list.
    # if i and j are same append "i" in result list
    # after updating value in res we will update i = j
    # we will do same outside loop once to get last pair or element

    def summaryRanges(self, nums: List[int]) -> List[str]:

        i = 0
        j = 1
        res = []

        if len(nums) == 0:
            return []

        while j < len(nums):

            if nums[j-1] == nums[j]-1:
                j += 1
            else:
                if i == j-1:
                    res.append(str(nums[i]))
                    i += 1
                else:
                    res.append(str(nums[i]) + "->" + str(nums[j-1]))
                    i = j
                j += 1
        
        if i == j-1:
            res.append(str(nums[i]))
            i += 1
        else:
            res.append(str(nums[i]) + "->"+ str(nums[j-1]))
            i = j
            j += 1

        return res
