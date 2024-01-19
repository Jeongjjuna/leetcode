class Solution:
    
    # 접근1. 이진 탐색 O(logN)
    def sol_1(self, numbers, target):
        p1, p2 = 0, len(numbers) - 1
        
        while p1 < p2:
            s = numbers[p1] + numbers[p2]
            
            if s > target:
                p2 -= 1
                
            elif s < target:
                p1 += 1
                
            elif s == target:
                break
                
        return [p1 + 1, p2 + 1]
    
    
    # 접근2. 해시 O(n)
    def sol_2(self, numbers, target):
        d = dict()
        
        for i, elem in enumerate(numbers):
            if target - elem in d:
                return [d[target - elem], i + 1]
            
            d[elem] = i + 1
                
        
    
    # O(NlogN)이하로 해결해야함
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.sol_2(numbers, target)
