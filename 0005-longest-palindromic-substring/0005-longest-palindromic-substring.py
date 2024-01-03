class Solution:
    
    def is_palindrom(self, s):    
        return s == s[::-1]
    
    
    def sol_1(self, s):                
        n = len(s)
        longest = 0
        ans = ''
        for i in range(n):
            for j in range(i, n):
                parsed = s[i : j + 1]
                if self.is_palindrom(parsed):
                    if longest < len(parsed):
                        longest = len(parsed)
                        ans = parsed 
        return ans
        
        
        
    
    def find_palindrom(self, s, i1, i2):
        
        max_len = 0
        ans = ''
        left, right = i1, i2
        while (0 <= left and right < len(s)):
            if s[left] == s[right]:
                max_len = right - left + 1
                ans = s[left:right + 1]
            else:
                break
            left -= 1
            right += 1
            
        return max_len, ans
            
        
        
    def sol_2(self, s):
        
        n = len(s)
        longest = 0
        ans = ''
        for i in range(n):
            length, palindrom = self.find_palindrom(s, i, i)
            if (longest < length):
                longest = length
                ans = palindrom
                
        for i in range(n - 1):
            length, palindrom = self.find_palindrom(s, i, i + 1)
            if (longest < length):
                longest = length
                ans = palindrom 
        return ans
       
        
    def longestPalindrome(self, s: str) -> str:
        # 접근1. 완전탐색 -> 시간초과
        # return self.sol_1(s)
    
        # 접근2. 가운데 i를 기준으로 양방향으로 팬린드롬 확인
        #        팰린드롬이 짝수인 경우도 추가로 구해줘야함.
        return self.sol_2(s)
    

    
    
