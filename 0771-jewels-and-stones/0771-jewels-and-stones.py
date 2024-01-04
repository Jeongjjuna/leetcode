class Solution:
    # 접근 1. 구현(완탐)
    def sol_1(self, jewels, stones):
        cnt = 0
        for elem in stones:
            if elem in jewels:
               cnt += 1
        return cnt
        
    
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return self.sol_1(jewels, stones);