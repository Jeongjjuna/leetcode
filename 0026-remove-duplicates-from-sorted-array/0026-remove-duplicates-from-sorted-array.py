class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 중복 요소를 모두 제거하기
        s = set(nums)

        idx = 0
        non_duplicate_nums = list(s)
        non_duplicate_nums.sort() # O(NlogN)
        for x in non_duplicate_nums: # O(N)
            nums[idx] = x
            idx += 1
            
        return len(s)