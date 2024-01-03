class Solution:
    
    # 접근1. 정렬 후 dict에 저장하기
    def sol_1(self, strs):
        answer = []
        
        d = dict()
        for elem in strs:
            key = "".join(sorted(elem))
            
            if not key in d:
                d[key] = []          
            d[key].append(elem)
    
 
        for key in d:
            answer.append(d[key])
    
        return answer
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.sol_1(strs)