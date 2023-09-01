class Solution:
    def swap(self, start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k = k % n

        # 전체를 뒤집어준다.
        self.swap(0, n - 1, nums)
        
        # k값 기준 왼쪽을 뒤집는다.
        self.swap(0, k - 1, nums)
        
        # k값 기준 오른쪽을 뒤집는다.
        self.swap(k , n - 1, nums)