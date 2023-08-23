class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx = 0
        for i in range(len(nums)):
            if i > len(nums) - 3:
                nums[idx] = nums[i]
                idx += 1
                continue
                
            if nums[i] != nums[i + 2]:
                nums[idx] = nums[i]
                idx += 1
        
        return idx