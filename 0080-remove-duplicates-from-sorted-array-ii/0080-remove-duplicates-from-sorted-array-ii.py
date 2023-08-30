class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx, n = 0, len(nums)
        for i in range(n - 2):
            if nums[i] != nums[i + 2]:
                nums[idx] = nums[i]
                idx += 1
                
        
        # 2개의 남은 숫자 넣기
        for i in range(max(0, n - 2), n):
            nums[idx] = nums[i]
            idx += 1
        
        
        return idx