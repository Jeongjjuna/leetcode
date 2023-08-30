class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 중복 요소를 모두 제거하기
        s = set(nums)


        non_duplicate_nums = list(s)
        non_duplicate_nums.sort() # O(NlogN)
        
        for i, x in enumerate(non_duplicate_nums): # O(N)
            nums[i] = x

            
        return len(s)