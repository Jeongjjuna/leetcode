import heapq

class Solution:
    
    # 접근1. 완전탐색
    # 시간복잡도 : O(n**2)
    # 실행시간 : 993ms
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
    
    
    # 접근2. 정렬
    # 시간복잡도 : O(nlogn)
    # 실행시간 : 53ms
    def sol_2(self, nums):
        nums.sort(reverse = True)
        return (nums[0] - 1) * (nums[1] - 1)
    
    
    # 접근3. 힙
    # 시간복잡도 : O(nlogn)
    # 실행시간 : 
    def sol_3(self, nums):
        hq = []
        for elem in nums:
            heapq.heappush(hq, -elem)
        
        max_val_1 = -heapq.heappop(hq)
        max_val_2 = -heapq.heappop(hq)

        return (max_val_1 - 1) * (max_val_2 - 1)
    
    
    def maxProduct(self, nums: List[int]) -> int:
        return self.sol_3(nums)
