class Solution:
    
    # 인접한 2개를 선택하지 않으면서
    # 최대값이 되도록 선택
    def sol_1(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            
        return dp[n - 1]
        
#         # dp[n] = n번째 수를 무조건 포함하면 서 0 ~ n사이의 문제조건 최대 합
#         for i in range(1, n):
            
#             std = nums[i]
#             for j in range(i - 1):
#                 std = max(std, dp[j] + nums[i])
#             dp[i] = std

#         return max(dp)
        
    
    def rob(self, nums: List[int]) -> int:
        return self.sol_1(nums)