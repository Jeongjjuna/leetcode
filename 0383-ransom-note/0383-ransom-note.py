class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        h = dict()
        
        # magazine의 각각 요소의 개수를 구해준다.
        for elem in magazine:
            if elem in h:
                h[elem] += 1
            else:
                h[elem] = 1
                
                
        # ransomNote의 각 요소를 h에서 하나씩 지워준다.
        for elem in ransomNote:
            # ransomeNote의 해당 요소가 magazine에 없다면 실패
            if elem not in h:
                return False
            
            # 더이상 사용할 수 있는(매칭되는) 요소가 없다면 실패
            if h[elem] == 0:
                return False
            
            h[elem] -= 1
            
            
        return True
        