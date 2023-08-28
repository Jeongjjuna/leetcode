class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        

        
        n = len(s)
        p1, p2 = 0, 1
        d = dict()
        d[s[0]] = True
        interval_len = 1
        max_interval_len = 1
        
        while p1 < n and p2 < n:
            
            # 현재 구간에 이미 있다면
            if s[p2] in d:
                del d[s[p1]]
                p1 += 1
                interval_len -= 1
            elif s[p2] not in d:
                if 0 <= p2 < n:
                    d[s[p2]] = True
                p2 += 1
                interval_len += 1
                
                max_interval_len = max(max_interval_len, interval_len)
                

        return max_interval_len