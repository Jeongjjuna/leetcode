class Solution:
    def jump(self, nums: List[int]) -> int:
        pre = 0
        jump = 0
        far = 0

        for i in range(len(nums)-1):
            far = max(far, nums[i] + i)            

            if i == pre:
                jump += 1
                pre = far


        return jump