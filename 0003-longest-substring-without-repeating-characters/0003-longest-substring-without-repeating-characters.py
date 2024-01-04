class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        ans = 0
        for i in range(n):
            # i에서 시작하는 가장 긴 서로다른 문자열
            d = dict()
            d[s[i]] = 1
            start = i
            end = i + 1
            while end < n:
                if s[end] in d:
                    break
                else:
                    d[s[end]] = 1
                    end += 1
                    
            ans = max(ans, end - start)
                    
        return ans
        