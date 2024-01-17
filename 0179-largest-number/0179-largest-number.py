from functools import cmp_to_key


class Solution:
        
    # 접근1. 우선순위를 직접 지정해주자.
    def sol_1(self, nums):
        
        def compare(x, y):
            # 맨 앞자리가 더 크면 앞으로
            if int(x[0]) > int(y[0]):
                return -1

            # 더 했을 때 더 클 때 x, y 순으로
            if int(x + y) > int(y + x):
                return -1
            
            return 0
        
    
        nums = list(map(str, nums))       
        nums.sort(key = cmp_to_key(compare)) 
        
        if nums[0] == "0":
            return "0"
        return "".join(nums)
        

    
    def largestNumber(self, nums: List[int]) -> str:
        return self.sol_1(nums)