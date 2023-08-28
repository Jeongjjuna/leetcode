class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        p1, p2 = 0, 0
        n = len(nums)
        min_interval = sys.maxsize
        s = nums[0]
        while p1 <= p2 and p1 < n and p2 < n:
            if s < target:
                p2 += 1
                if 0 <= p2 <n:
                    s += nums[p2]
                
            elif s >= target:
                min_interval = min(min_interval, p2 - p1 + 1)
                s -= nums[p1]
                p1 += 1
                
        
        # 
        if min_interval == sys.maxsize:
            return 0
        else:    
            return min_interval
                    