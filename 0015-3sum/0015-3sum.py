class Solution:
    
    # 접근1. 완전탐색 O(N**3) -> 시간초과
    def sol_1(self, nums):
        answer = []
        s = set()
        n = len(nums)
        
        nums.sort()
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        s.add((nums[i], nums[j], nums[k]))
        
        for x in list(s):
            answer.append(list(x))
        
        return answer
    
    
    def add_triplets(self, i, nums, s):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            two_sum = nums[left] + nums[right]
            
            if two_sum == -nums[i]:
                s.add((nums[i], nums[left], nums[right]))
                left += 1
            elif two_sum < -nums[i]:
                left += 1
            elif two_sum > -nums[i]:
                right -= 1
        
    
    
    # 접근2. 투포인터
    def sol_2(self, nums):
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        
        
        n = len(nums)
        s = set()
        answer = []
        
        for i in range(n - 2):
            self.add_triplets(i, nums, s)      

        for x in list(s):
            answer.append(list(x))
        
        return answer
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.sol_2(nums)

    
