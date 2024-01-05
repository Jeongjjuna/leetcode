class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        # 접근1. 완전탐색
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                val = (nums[i]-1)*(nums[j]-1)
                ans = max(ans, val)
                
        return ans