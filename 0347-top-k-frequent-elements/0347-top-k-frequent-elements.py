from collections import defaultdict
import heapq

class Solution:
    
    # 접근1. 해시 -> O(nlogn)
    def sol_1(self, nums, k):
        
        # 해시에 개수를 저장 O(n)
        d = defaultdict(int)
        for elem in nums:
            d[elem] += 1
            
        # 개수 내림차순으로 정렬 O(nlogn)
        desc = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        # k개만큼 값 뽑기
        answer = []
        for i in range(k):
            answer.append(desc[i][0])
        
        return answer
    
    
    # 접근2. -> O(nlogn)보다 더 좋은 시간복잡도 ... 우선순위 힙?
    def sol_2(self, nums, k):
        # 해시에 개수를 저장 O(n)
        d = defaultdict(int)
        for elem in nums:
            d[elem] += 1
            
        hq = []
        for key in d:
            heapq.heappush(hq, (-d[key], key))
        
        answer = []
        for _ in range(k):
            pri, val = heapq.heappop(hq)
            answer.append(val)
        
        return answer
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.sol_2(nums, k)