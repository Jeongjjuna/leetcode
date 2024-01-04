class Solution:
    
    # 접근1. 해시를 이용한 완전탐색 -> O(n**2)
    def sol_1(self, s):
        n = len(s)
        ans = 0
        for i in range(n): # O(n)
            # i에서 시작하는 가장 긴 서로다른 문자열
            d = dict()
            d[s[i]] = 1
            start = i
            end = i + 1
            while end < n:# O(n)
                if s[end] in d:
                    break
                else:
                    d[s[end]] = 1
                    end += 1
                    
            ans = max(ans, end - start)
                    
        return ans
    
    
    # 접근2. 투포인터 -> O(n)
    def sol_2(self, s):
        n = len(s)
        cnt = 0
        ans = 0
        d = dict()
        left, right = 0, 0
        
        while left < n and right < n:
            if s[right] in d:
                del d[s[left]]
                left += 1
                cnt -= 1
            else:
                d[s[right]] = 1
                right += 1
                cnt += 1
            
            ans = max(ans, cnt)
            
        return ans
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.sol_2(s)

        