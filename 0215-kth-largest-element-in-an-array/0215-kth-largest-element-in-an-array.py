import heapq
from collections import defaultdict

# 배열에서 k번째로 큰 요소
# n = 100000
# O(nlogn)까지 가능


class Solution:
 
    # 접근1. 힙 -> 정렬사용해도 똑같음
    # 시간복잡도 : O(nlogn)
    # 실행시간 : 515ms
    def sol_1(self, nums, k):
        hq = []
        for elem in nums:
            heapq.heappush(hq, -elem)
        
        for _ in range(k):
            val = -heapq.heappop(hq)
        
        return val
    
    
    
    # nums[i]가 최대 10000
    # 카운팅정렬해볼까?
    def sol_2(self, nums, k):
        d = defaultdict(int)
        
        max_val = 0
        min_val = 10001
        for elem in nums:
            d[elem] += 1
            max_val = max(max_val, elem)
            min_val = min(min_val, elem)
        
        temp = k
        for i in range(max_val, min_val - 1, -1):
            if i not in d:
                continue
                
            if temp <= d[i]:
                return i
            
            temp -= d[i]
     
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.sol_2(nums, k) 