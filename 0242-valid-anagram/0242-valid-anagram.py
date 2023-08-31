class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h = defaultdict(int)
        for elem in s:
            h[elem] += 1
            
        for elem in t:
            if elem not in h:
                return False
            
            if h[elem] == 0:
                return False
            
            h[elem] -= 1
            
        # 만약 전체를 순회하며 남아있는 수가 있다면 실패
        for elem in s:
            if h[elem] != 0:
                return False
        
            
        return True