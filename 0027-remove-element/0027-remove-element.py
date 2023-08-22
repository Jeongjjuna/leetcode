class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        result = []
        for i in range(len(nums)): #O(100)
            if nums[i] == val:
                continue
                  
            result.append(nums[i])

        for i in range(len(nums)): #O(100)
            if i < len(result):
                nums[i] = result[i]

        
        return len(result)