class Solution:
    def swap_reverse(self, nums, start, end):
        while(start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.swap_reverse(nums, 0, n - 1)
        self.swap_reverse(nums, 0, k - 1)
        self.swap_reverse(nums, k, n - 1)
        
        