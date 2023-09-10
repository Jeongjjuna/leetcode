class Solution:
    
    ans = sys.maxsize
    
    # [start, end] 구간에서의 조건에 맞는 값 찾기
    def binary_search(self, start, end, cum_sum, nums, target):
        fixed_start = start
        
        # print(fixed_start, " -> ",end)
        
        while start <= end:
            mid = (start + end) // 2
            k = cum_sum[mid] - cum_sum[fixed_start] + nums[fixed_start]
            
            if k >= target:
                end = mid - 1
                self.ans = min(self.ans, abs(mid- fixed_start) + 1)
            elif k < target:
                start = mid + 1


    
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # 누적합구하기
        cum_sum = [0]*len(nums)
        cum_sum[0] = nums[0]
        for i in range(1, len(nums)):
            cum_sum[i] = cum_sum[i - 1] + nums[i]
            
        
        # 시작점고르기
        for start in range(len(nums)):
            self.binary_search(start, len(nums) - 1, cum_sum, nums, target)
        
        
        if self.ans == sys.maxsize:
            return 0
        else:
            return self.ans
