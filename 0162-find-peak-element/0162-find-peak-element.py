class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        INF = sys.maxsize
        
        # 배열의 요소가 1개일 경우는 그 값이 Peak
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            b = nums[mid]
            if mid == len(nums) - 1:
                a = nums[mid - 1]
                c = -INF
            elif mid == 0:
                a = -INF
                c = nums[mid + 1]
            else:
                a, c = nums[mid - 1], nums[mid + 1]
            
            if b < c:
                left = mid + 1
            elif a > b:
                right = mid - 1
            else:
                return mid