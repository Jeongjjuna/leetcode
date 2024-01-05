import heapq

# 배열에서 k번째로 큰 요소
# n = 100000
# O(nlogn)까지 가능


class Solution:
 
    # 접근1. 힙 -> 정렬사용해도 똑같음
    # 시간복잡도 : O(nlogn)
    # 실행시간 : ?
    def sol_1(self, nums, k):
        hq = []
        for elem in nums:
            heapq.heappush(hq, -elem)
        
        for _ in range(k):
            val = -heapq.heappop(hq)
        
        return val
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.sol_1(nums, k)