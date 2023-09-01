class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_idx = 0 # 최대로 이동가능한 거리
        
        for i in range(n):
            if i > max_idx:
                break
            
            if i <= max_idx and i + nums[i] >= n - 1:
                return True
            
            max_idx = max(max_idx, i + nums[i])
            
        return False