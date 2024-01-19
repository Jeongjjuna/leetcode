class Solution:
    
    # 접근1. 투포인터 O(N)
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
    
    
    # 접근2. 해시 O(N)
    def sol_2(self, numbers, target):
        d = dict()
        
        for i, elem in enumerate(numbers):
            if target - elem in d:
                return [d[target - elem], i + 1]
            
            d[elem] = i + 1
        
        
    # 접근3. 이진탐색 O(NlogN)
    def sol_3(self, numbers, target):
        
        def find_value(numbers, left, right):
            left, right = i + 1, len(numbers) - 1
            expected = target - elem
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == expected: # 찾았다면 해당 index를 반환합니다.
                    idx = mid
                    break

                if numbers[mid] > expected:
                    right = mid - 1  
                else:           
                    left = mid + 1       
            return idx
        
        for i, elem in enumerate(numbers):
            idx = find_value(numbers, i + 1, len(numbers) - 1)
            if idx == -1:
                continue
            return [i + 1, idx + 1]
        
    
    # O(NlogN)이하로 해결해야함
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.sol_3(numbers, target)
