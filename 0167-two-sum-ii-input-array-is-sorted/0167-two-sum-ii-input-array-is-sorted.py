class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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