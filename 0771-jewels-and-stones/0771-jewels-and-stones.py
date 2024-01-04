class Solution:
    # 접근1. 구현(완탐) -> O(n**2)
    def sol_1(self, jewels, stones):
        cnt = 0
        for elem in stones: # O(n)
            if elem in jewels: # O(n)
               cnt += 1
        return cnt

    
    # 접근2. 해시 -> O(n) + O(n) + O(1) = O(n)
    def sol_2(self, jewels, stones):
        # 사전에 값 넣기
        d = dict()
        for elem in jewels: # O(n)
            d[elem] = 1
            
        # 사전에 존재하는지 확인하기
        cnt = 0
        for elem in stones: # O(n)
            if elem in d: # O(1)
                cnt += 1
        return cnt
    
    # 접근2. 집합 set -> O(n) + O(n) + O(1) = O(n)
    def sol_3(self, jewels, stones):
        # 사전에 값 넣기
        s = set()
        for elem in jewels: # O(n)
            s.add(elem)
            
        # 사전에 존재하는지 확인하기
        cnt = 0
        for elem in stones: # O(n)
            if elem in s: # O(1)
                cnt += 1
        return cnt
    
    
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return self.sol_3(jewels, stones);