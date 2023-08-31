class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [2, 7, 11, 15]
        h = dict() # {data : index} = {2 : 0, 7 : 1, 11 : 2 ...}
        for i in range(len(nums)):
            elem = nums[i]
            if target - elem in h:
                return [h[target - elem], i]
            
            h[elem] = i
                