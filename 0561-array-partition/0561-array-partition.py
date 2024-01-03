class Solution(object):
    def sol_1(self, nums):
        nums.sort()
        
        n = len(nums)
        ans = 0
        for i in range(0, n, 2):
            ans += min(nums[i], nums[i + 1])
        
        return ans
        
        
    
    def arrayPairSum(self, nums):
        
        # 접근1. 정렬하기
        return self.sol_1(nums)
        