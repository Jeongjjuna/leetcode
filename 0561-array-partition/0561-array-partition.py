class Solution(object):
    
    # 접근1. 정렬하기(그리디)
    def sol_1(self, nums):
        
        # 변수 선언
        n, ans = len(nums), 0
        
        # 오름차순 정렬
        nums.sort()
        
        # 앞에서부터 2개씩 묶는다.
        for i in range(0, n, 2):
            ans += min(nums[i], nums[i + 1])
        
        return ans
        
        
    
    def arrayPairSum(self, nums):
        
        return self.sol_1(nums)