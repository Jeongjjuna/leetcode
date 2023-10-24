class Solution:
    
    def hIndex(self, citations: List[int]) -> int:
        
        # 접근 2. 카운팅 정렬
        MAX_VAL = 1001
        count = [0] * MAX_VAL
        max_c = max(citations)
        
        for i in range(0, max_c + 1):
            c = 0
            for x in citations:
                if i <= x:
                    c += 1
            count[i] = c
        
        ans = 0
        for i in range(max_c + 1):
            if count[i] >= i:
                ans = i
        return ans
            