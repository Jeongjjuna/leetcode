class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # 배열의 요소가 1개일 경우는 그 값이 Peak
        if len(nums) == 1:
            return 0
        
        INF = sys.maxsize
        for i in range(len(nums)):
            if i == 0:
                if -INF < nums[i]  and nums[i + 1] < nums[i]:
                    return i
                
            if i == len(nums) - 1:
                if nums[i - 1] < nums[i]  and -INF < nums[i]:
                     return i
            
            if nums[i - 1] < nums[i]  and nums[i + 1] < nums[i]:
                return i