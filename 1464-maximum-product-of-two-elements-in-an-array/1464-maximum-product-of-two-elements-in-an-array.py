class Solution:
    
    # 접근1. 완전탐색 -> O(n**2)
    def sol_1(self, nums):        
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                val = (nums[i]-1)*(nums[j]-1)
                ans = max(ans, val)
                
        return ans
    
    # 접근2. 정렬 -> O(nlogn)
    def sol_2(self, nums):
        nums.sort(reverse = True)
        return (nums[0] - 1) * (nums[1] - 1)
    
    
    def maxProduct(self, nums: List[int]) -> int:
        return self.sol_2(nums)
