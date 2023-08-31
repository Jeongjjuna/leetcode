class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        h = dict()
        for i in range(len(nums)):
            elem = nums[i]
            
            if elem in h:
                if abs(h[elem] - i) <= k:
                    return True
                
            h[elem] = i
            
        return False