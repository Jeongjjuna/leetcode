class Solution:
    

    # 접근1. Follow up -> 카운팅정렬
    def sol_1(self, nums):
        
        count = defaultdict(int)
        for elem in nums:
            count[elem] += 1
        
        print(count)
        idx = 0
        for i in range(3):
            
            while count[i] > 0:
                nums[idx] = i
                idx += 1
                count[i] -= 1
            
            
            
            
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sol_1(nums)
        